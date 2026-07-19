"""SessionStart hook: injects learner-state context into the transcript.

Stdlib only. Imports the engine package by walking up two parents from this
file's resolved location (hooks/scripts/session_start.py -> repo root).
"""

import json
import os
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

try:
    from engine import scheduler, state  # noqa: E402
except Exception:  # broken/partial install: fail open, never block the session
    scheduler = state = None

# Phase -> named misconception id, per SG Part VIII.
MISCONCEPTIONS = {
    "phase1": "completeness-implies-convergence",
    "phase2": "compact-iff-closed-and-bounded",
    "phase3": "consecutive-closeness-implies-convergence",
    "phase4": "pencil-lifting-image",
    "phase5": "continuity-implies-uniform-continuity",
    "phase6": "terms-to-zero-implies-convergence",
    "phase7": "pointwise-limit-preserves-continuity",
}

FIRST_RUN_DIRECTIVE = """FIRST RUN: This is a new learner workspace with no learner.json yet.

On the user's first message this session, introduce yourself and run the
real-analysis-tutor:tutor skill's onboarding interview. Volunteer everything
up front — do not wait to be asked:
- You will create the workspace files (learner.json, reviews.json, ledger.json).
- You will offer to set up Lean 4 verification.
- You will never hand over proofs; you guide via Socratic questioning only.

Use the real-analysis-tutor:tutor skill to orchestrate."""

NO_WORKSPACE_DIRECTIVE = (
    "real-analysis-tutor plugin note: no study workspace exists yet. A "
    "greeting alone is not intent — respond to it normally. Only if the "
    "user explicitly asks to study or learn Real Analysis, mathematics, or "
    "proofs should you introduce yourself and run the "
    "real-analysis-tutor:tutor onboarding interview. Otherwise do not "
    "mention the tutor."
)


def _pointer_remote_directive(ws: Path, today: date) -> str:
    """Soft, conditional directive for a workspace that resolved only via
    the `~/.claude/real-analysis-tutor.json` pointer file — cwd is not
    inside the workspace itself. Unlike the local returning-learner ritual,
    this does not command an open ritual; it hands the model a one-line
    summary and lets it decide from the user's actual message.
    """
    s = state.load_state(ws)
    reviews = scheduler.load_reviews(ws)
    due = scheduler.due(reviews, today)
    phase = (s.get("position", {}) or {}).get("phase") or "prelim"

    return (
        f"real-analysis-tutor plugin note: a study workspace exists at {ws}, "
        "found via the pointer file (this session is not inside it).\n"
        "Subject: Real Analysis\n"
        f"Phase: {phase} · Due reviews: {len(due)}\n\n"
        "If the user's message relates to studying Real Analysis, "
        "mathematics, proofs, or continuing their coursework, deliver the "
        "session-open ritual and proceed (use the real-analysis-tutor:tutor "
        "skill). Otherwise do not mention the tutor."
    )


def build_context(cwd: Path, today: date) -> str | None:
    """Pure function: given a cwd and today's date, return the additionalContext
    string for the SessionStart hook. Location-aware: a workspace found by
    walking up from cwd (the learner is "in" it) gets the full local
    directives unchanged; a workspace resolved only via the pointer file
    gets a soft conditional nudge instead of the full open ritual; no
    workspace at all gets a small conditional directive, gated on explicit
    intent, instead of None.
    """
    local_ws = state.find_workspace_local(cwd)
    ws = local_ws if local_ws is not None else state.find_workspace(cwd)
    if ws is None:
        return NO_WORKSPACE_DIRECTIVE

    if local_ws is None:
        return _pointer_remote_directive(ws, today)

    learner_path = Path(ws) / "learner.json"
    if not learner_path.exists():
        return FIRST_RUN_DIRECTIVE

    s = state.load_state(ws)
    reviews = scheduler.load_reviews(ws)
    due = scheduler.due(reviews, today)
    digest = state.state_digest(s, due)

    phase = (s.get("position", {}) or {}).get("phase")
    misconception = MISCONCEPTIONS.get(phase)

    lines = [
        "RETURNING LEARNER — open ritual required.",
        "On the user's first message this session — whatever it says — first "
        "deliver the session-open ritual: greet, state summary, due reviews, "
        "propose today's agenda; then address their message.",
        "",
        digest,
    ]
    if phase:
        if misconception:
            lines.append(f"Current phase: {phase} (named misconception: {misconception})")
        else:
            lines.append(f"Current phase: {phase}")
    lines.append("")
    lines.append("Use the real-analysis-tutor:tutor skill to orchestrate.")

    return "\n".join(lines)


def _log_error(exc: Exception) -> None:
    log_dir = os.environ.get("CLAUDE_PLUGIN_DATA")
    if not log_dir:
        return
    try:
        log_path = Path(log_dir) / "errors.log"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with log_path.open("a") as f:
            f.write(f"session_start.py: {exc!r}\n")
    except Exception:
        pass


def main() -> None:
    try:
        raw = sys.stdin.read()
        try:
            payload = json.loads(raw)
        except (json.JSONDecodeError, ValueError):
            # Unparseable stdin: stay silent, exit 0. Do not fabricate a cwd
            # fallback for input we could not understand at all.
            return

        if not isinstance(payload, dict):
            return

        if state is None or scheduler is None:
            return
        cwd = Path(payload.get("cwd") or Path.cwd())
        context = build_context(cwd, date.today())

        if context is not None:
            output = {
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": context,
                }
            }
            print(json.dumps(output))
    except Exception as exc:  # fail open: never block the session
        try:
            _log_error(exc)
        except Exception:
            pass


if __name__ == "__main__":
    main()
