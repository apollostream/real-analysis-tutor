"""Stop hook: reminds Claude to persist learner state when the session's
learner.json has gone stale (i.e. proof work / assessments / errors likely
happened without being written back). Fails open on any error.

The reminder fires AT MOST ONCE PER SESSION: a sentinel file in the
workspace records which session has already been reminded, so a stale
learner.json (e.g. after an overnight gap) does not nag on every turn.

Stdlib only.
"""

import datetime
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
try:
    from engine import state  # noqa: E402
except Exception:  # broken/partial install: fail open, never block the session
    state = None

STALE_SECONDS = 30 * 60
SENTINEL = ".stop-reminder-session"

REASON = (
    "Before finishing: if this exchange produced proof work, assessment "
    "results, review grades, or errors, persist them now — update "
    "learner.json / ledger.json / error_log.json / reviews.json via the "
    "tutor's close ritual. Then stop. (This reminder fires once per "
    "session; if there is nothing new to persist, simply stop.)"
)


def _session_key(session_id) -> str:
    # No session id -> fall back to a day key so the reminder still fires
    # at most once per day rather than never or every turn.
    return str(session_id) if session_id else "day-" + datetime.date.today().isoformat()


def _already_reminded(ws: Path, session_id) -> bool:
    try:
        return (Path(ws) / SENTINEL).read_text().strip() == _session_key(session_id)
    except OSError:
        return False


def record_reminded(ws: Path, session_id) -> None:
    try:
        (Path(ws) / SENTINEL).write_text(_session_key(session_id))
    except OSError:
        pass


def should_remind(ws: Path | None, now_ts: float, stop_hook_active: bool, session_id) -> bool:
    if ws is None:
        return False
    if stop_hook_active:
        return False
    learner_path = Path(ws) / "learner.json"
    if not learner_path.exists():
        return False
    if _already_reminded(ws, session_id):
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

        if state is None:
            sys.exit(0)
        cwd = payload.get("cwd") or str(Path.cwd())
        stop_hook_active = bool(payload.get("stop_hook_active", False))
        session_id = payload.get("session_id")

        ws = state.find_workspace(Path(cwd))

        if should_remind(ws, time.time(), stop_hook_active, session_id):
            record_reminded(ws, session_id)
            print(json.dumps({"decision": "block", "reason": REASON}))
    except Exception:
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
