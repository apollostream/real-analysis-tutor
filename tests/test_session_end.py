import sys
import time
from pathlib import Path
from engine import state

sys.path.insert(0, str(Path("hooks/scripts")))
import session_end  # noqa: E402


def make_ws(tmp_path, stale_minutes):
    (tmp_path / state.MARKER).write_text("{}")
    p = tmp_path / "learner.json"
    p.write_text("{}")
    import os
    old = time.time() - stale_minutes * 60
    os.utime(p, (old, old))
    return tmp_path


def test_stale_state_triggers(tmp_path):
    ws = make_ws(tmp_path, 45)
    assert session_end.should_remind(ws, time.time(), False)


def test_fresh_state_no_trigger(tmp_path):
    ws = make_ws(tmp_path, 5)
    assert not session_end.should_remind(ws, time.time(), False)


def test_loop_guard(tmp_path):
    ws = make_ws(tmp_path, 45)
    assert not session_end.should_remind(ws, time.time(), True)


def test_no_workspace_no_trigger():
    assert not session_end.should_remind(None, time.time(), False)
