import json
from pathlib import Path
from engine import state


def make_ws(tmp_path):
    (tmp_path / state.MARKER).write_text('{"schema_version": 1, "curriculum": "real-analysis"}')
    return tmp_path


def test_default_state_shape():
    s = state.default_state()
    assert s["schema_version"] == 1
    assert s["position"] == {"phase": "prelim", "chapter": None, "rung": 1}
    assert s["concepts"] == {} and s["stuck"] == {} and s["misconception_log"] == []
    assert s["session_count"] == 0 and s["profile"] is None


def test_find_workspace_walks_up(tmp_path):
    ws = make_ws(tmp_path)
    deep = ws / "a" / "b"
    deep.mkdir(parents=True)
    assert state.find_workspace(deep) == ws


def test_find_workspace_none(tmp_path, monkeypatch):
    monkeypatch.setenv("HOME", str(tmp_path / "nohome"))
    assert state.find_workspace(tmp_path) is None


def test_find_workspace_local_walks_up(tmp_path):
    ws = make_ws(tmp_path)
    deep = ws / "a" / "b"
    deep.mkdir(parents=True)
    assert state.find_workspace_local(deep) == ws


def test_find_workspace_local_none_when_only_pointer_resolves(tmp_path, monkeypatch):
    # Workspace lives elsewhere; only the pointer file knows about it. A cwd
    # with no marker in its own ancestry must not resolve locally, even
    # though find_workspace (with the pointer fallback) would find it.
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    ws = make_ws(elsewhere)
    home = tmp_path / "home"
    (home / ".claude").mkdir(parents=True)
    (home / ".claude" / "real-analysis-tutor.json").write_text(
        json.dumps({"workspace": str(ws)})
    )
    monkeypatch.setenv("HOME", str(home))

    foreign_cwd = tmp_path / "foreign"
    foreign_cwd.mkdir()

    assert state.find_workspace_local(foreign_cwd) is None
    assert state.find_workspace(foreign_cwd) == ws


def test_load_missing_returns_default(tmp_path):
    ws = make_ws(tmp_path)
    assert state.load_state(ws)["session_count"] == 0


def test_save_then_load_roundtrip(tmp_path):
    ws = make_ws(tmp_path)
    s = state.default_state()
    s["session_count"] = 7
    state.save_state(ws, s)
    assert state.load_state(ws)["session_count"] == 7
    assert not (ws / "learner.json.tmp").exists()


def test_corrupt_state_backed_up(tmp_path):
    ws = make_ws(tmp_path)
    (ws / "learner.json").write_text("{not json")
    s = state.load_state(ws)
    assert s["session_count"] == 0
    assert list(ws.glob("learner.json.corrupt-*"))


def test_digest_mentions_position_and_due():
    s = state.default_state()
    s["position"] = {"phase": "phase4", "chapter": "Rudin Ch.4", "rung": 3}
    d = state.state_digest(s, ["heine_cantor", "ivt"])
    assert "phase4" in d and "heine_cantor" in d and len(d.splitlines()) <= 6
