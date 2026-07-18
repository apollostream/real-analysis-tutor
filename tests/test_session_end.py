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
    assert session_end.should_remind(ws, time.time(), False, "s1")


def test_fresh_state_no_trigger(tmp_path):
    ws = make_ws(tmp_path, 5)
    assert not session_end.should_remind(ws, time.time(), False, "s1")


def test_loop_guard(tmp_path):
    ws = make_ws(tmp_path, 45)
    assert not session_end.should_remind(ws, time.time(), True, "s1")


def test_no_workspace_no_trigger():
    assert not session_end.should_remind(None, time.time(), False, "s1")


def test_reminds_at_most_once_per_session(tmp_path):
    ws = make_ws(tmp_path, 45)
    assert session_end.should_remind(ws, time.time(), False, "s1")
    session_end.record_reminded(ws, "s1")
    assert not session_end.should_remind(ws, time.time(), False, "s1")


def test_new_session_reminds_again(tmp_path):
    ws = make_ws(tmp_path, 45)
    session_end.record_reminded(ws, "s1")
    assert session_end.should_remind(ws, time.time(), False, "s2")


def test_missing_session_id_uses_day_key(tmp_path):
    ws = make_ws(tmp_path, 45)
    assert session_end.should_remind(ws, time.time(), False, None)
    session_end.record_reminded(ws, None)
    assert not session_end.should_remind(ws, time.time(), False, None)
