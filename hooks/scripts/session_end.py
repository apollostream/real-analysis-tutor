"""Stop hook: reminds Claude to persist learner state when the session's
learner.json has gone stale (i.e. proof work / assessments / errors likely
happened without being written back). Fails open on any error.

Stdlib only.
"""

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from engine import state  # noqa: E402

STALE_SECONDS = 30 * 60

REASON = (
    "Before finishing: if this exchange produced proof work, assessment "
    "results, review grades, or errors, persist them now — update "
    "learner.json / ledger.json / error_log.json / reviews.json via the "
    "tutor's close ritual. Then stop."
)


def should_remind(ws: Path | None, now_ts: float, stop_hook_active: bool) -> bool:
    if ws is None:
        return False
    if stop_hook_active:
        return False
    learner_path = Path(ws) / "learner.json"
    if not learner_path.exists():
        return False
    mtime = learner_path.stat().st_mtime
    return (now_ts - mtime) > STALE_SECONDS


def main() -> None:
    try:
        raw = sys.stdin.read()
        try:
            payload = json.loads(raw) if raw.strip() else {}
        except json.JSONDecodeError:
            payload = {}

        cwd = payload.get("cwd") or str(Path.cwd())
        stop_hook_active = bool(payload.get("stop_hook_active", False))

        ws = state.find_workspace(Path(cwd))

        if should_remind(ws, time.time(), stop_hook_active):
            print(json.dumps({"decision": "block", "reason": REASON}))
    except Exception:
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
