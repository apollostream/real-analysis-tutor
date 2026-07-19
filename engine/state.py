"""Learner state engine: workspace discovery, atomic persistence, and a
short digest of learner state for hook injection.

Stdlib only: json, os, datetime, pathlib.
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

MARKER = ".ra-tutor-workspace"


def find_workspace_local(start: Path) -> Path | None:
    """Walk `start` and its ancestors looking for MARKER. Does not consult
    the `~/.claude/real-analysis-tutor.json` pointer — a non-None result
    here means the workspace was found because `start` is inside it, not
    because a pointer file said so elsewhere. Returns None on any failure
    or if nothing is found — never raises.
    """
    try:
        current = Path(start).resolve()
    except Exception:
        return None

    try:
        candidates = [current, *current.parents]
        for candidate in candidates:
            try:
                if (candidate / MARKER).exists():
                    return candidate
            except Exception:
                continue
    except Exception:
        pass

    return None


def find_workspace(start: Path) -> Path | None:
    """Walk `start` and its ancestors looking for MARKER. If none is found,
    fall back to reading `~/.claude/real-analysis-tutor.json`'s "workspace"
    key and returning that Path if its marker exists. Returns None on any
    failure or if nothing is found — never raises.
    """
    local = find_workspace_local(start)
    if local is not None:
        return local

    try:
        config_path = Path.home() / ".claude" / "real-analysis-tutor.json"
        if not config_path.exists():
            return None
        data = json.loads(config_path.read_text())
        workspace = data.get("workspace")
        if not workspace:
            return None
        ws_path = Path(workspace)
        if (ws_path / MARKER).exists():
            return ws_path
        return None
    except Exception:
        return None


def default_state() -> dict:
    return {
        "schema_version": 1,
        "position": {"phase": "prelim", "chapter": None, "rung": 1},
        "concepts": {},
        "stuck": {},
        "misconception_log": [],
        "session_count": 0,
        "profile": None,
    }


def load_state(workspace: Path) -> dict:
    path = Path(workspace) / "learner.json"
    if not path.exists():
        return default_state()

    try:
        return json.loads(path.read_text())
    except (json.JSONDecodeError, OSError, UnicodeDecodeError):
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        corrupt_path = Path(workspace) / f"learner.json.corrupt-{timestamp}"
        try:
            path.rename(corrupt_path)
        except OSError:
            pass
        return default_state()


def save_state(workspace: Path, state: dict) -> None:
    workspace = Path(workspace)
    tmp_path = workspace / "learner.json.tmp"
    final_path = workspace / "learner.json"
    tmp_path.write_text(json.dumps(state, indent=2))
    os.replace(tmp_path, final_path)


def state_digest(state: dict, due: list[str]) -> str:
    lines = []

    position = state.get("position", {}) or {}
    phase = position.get("phase")
    chapter = position.get("chapter")
    rung = position.get("rung")
    lines.append(f"Position: phase={phase} chapter={chapter} rung={rung}")

    lines.append(f"Sessions completed: {state.get('session_count', 0)}")

    concepts = state.get("concepts", {}) or {}
    weak = []
    for name, info in concepts.items():
        mastery = info.get("mastery") if isinstance(info, dict) else info
        if isinstance(mastery, (int, float)):
            weak.append((mastery, name))
    weak.sort(key=lambda pair: pair[0])
    weakest_names = [name for _, name in weak[:3]]
    if weakest_names:
        lines.append(f"Weakest concepts: {', '.join(weakest_names)}")

    if due:
        lines.append(f"Due for review: {', '.join(due)}")

    return "\n".join(lines[:6])
