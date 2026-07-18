import datetime
import json
import subprocess
import sys
from pathlib import Path
from engine import state

SCRIPT = Path("hooks/scripts/session_start.py")
D0 = datetime.date(2026, 7, 17)
sys.path.insert(0, str(SCRIPT.parent))
import session_start  # noqa: E402


def make_ws(tmp_path):
    (tmp_path / state.MARKER).write_text('{"schema_version": 1, "curriculum": "real-analysis"}')
    return tmp_path


def test_no_workspace_returns_install_directive(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))
    ctx = session_start.build_context(tmp_path, D0)
    assert "no study workspace" in ctx
    assert "Otherwise do not mention the tutor" in ctx


def test_first_run_directive(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))
    ws = make_ws(tmp_path)  # marker but no learner.json => first run
    ctx = session_start.build_context(ws, D0)
    assert "FIRST RUN" in ctx and "onboarding" in ctx.lower()


def test_returning_learner_open_ritual(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path))
    ws = make_ws(tmp_path)
    s = state.default_state()
    s["position"] = {"phase": "phase4", "chapter": "Rudin Ch.4", "rung": 2}
    s["session_count"] = 3
    state.save_state(ws, s)
    ctx = session_start.build_context(ws, D0)
    assert "open ritual" in ctx.lower()
    assert "phase4" in ctx
    assert "first message" in ctx.lower()  # speak-first instruction


def test_process_emits_json_and_exits_zero(tmp_path):
    ws = make_ws(tmp_path)
    out = subprocess.run(
        [sys.executable, str(SCRIPT.resolve())],
        input=json.dumps({"cwd": str(ws)}), capture_output=True, text=True, cwd=ws)
    assert out.returncode == 0
    payload = json.loads(out.stdout)
    assert payload["hookSpecificOutput"]["hookEventName"] == "SessionStart"


def test_fail_open_on_garbage_stdin():
    out = subprocess.run([sys.executable, str(SCRIPT.resolve())],
                         input="not json", capture_output=True, text=True)
    assert out.returncode == 0 and out.stdout.strip() == ""
