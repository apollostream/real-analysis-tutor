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
    "real-analysis-tutor plugin note: no study workspace exists yet. If the "
    "user's message suggests they want to study Real Analysis, proofs, "
    "Rudin, or math learning — or they greet you with intent to start — "
    "introduce yourself and run the real-analysis-tutor:tutor onboarding "
    "interview. Otherwise do not mention the tutor."
)


def build_context(cwd: Path, today: date) -> str | None:
    """Pure function: given a cwd and today's date, return the additionalContext
    string for the SessionStart hook. When no workspace is found, returns a
    small conditional directive instead of None so the model knows to offer
    onboarding only when the learner's intent warrants it.
    """
    ws = state.find_workspace(cwd)
    if ws is None:
        return NO_WORKSPACE_DIRECTIVE

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
