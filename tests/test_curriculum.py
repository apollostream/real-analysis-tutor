import yaml
from pathlib import Path
from engine import ledger

ROOT = Path("curriculum/real-analysis")
REQUIRE_ALL = False  # Task 12 flips to True


def load_yaml(rel):
    p = ROOT / rel
    if not p.exists():
        if REQUIRE_ALL:
            raise AssertionError(f"missing curriculum file: {rel}")
        import pytest
        pytest.skip(f"{rel} not authored yet")
    return yaml.safe_load(p.read_text())


def test_ledger_schema_matches_engine():
    doc = load_yaml("ledger-schema.yaml")
    assert [f["name"] for f in doc["fields"]] == list(ledger.LEDGER_FIELDS)
    assert [c["name"] for c in doc["error_categories"]] == list(ledger.ERROR_CATEGORIES)


def test_misconceptions_complete():
    doc = load_yaml("misconceptions.yaml")
    ids = {m["id"] for m in doc["misconceptions"]}
    assert ids == {
        "completeness-implies-convergence", "compact-iff-closed-and-bounded",
        "consecutive-closeness-implies-convergence", "pencil-lifting-image",
        "continuity-implies-uniform-continuity", "terms-to-zero-implies-convergence",
        "pointwise-limit-preserves-continuity"}
    for m in doc["misconceptions"]:
        for k in ("statement", "corrupted_step", "refutation", "counterexample", "phase", "topic"):
            assert m.get(k), f"{m['id']} missing {k}"


def test_curriculum_phases():
    doc = load_yaml("curriculum.yaml")
    ids = [p["id"] for p in doc["phases"]]
    assert ids == ["prelim"] + [f"phase{i}" for i in range(1, 10)]
    for p in doc["phases"]:
        assert p["texts"] and p["weeks"] and p["name"]
    misc = {p["id"]: p.get("misconception") for p in doc["phases"]}
    assert misc["phase4"] == "pencil-lifting-image"
    assert misc["phase8"] is None and misc["phase9"] is None and misc["prelim"] is None


def test_checklists_shape():
    for i in range(1, 8):
        doc = load_yaml(f"checklists/phase{i}.yaml")
        for k in ("phase", "topic", "items", "converse_checks", "lean_targets",
                  "rudin_exercises", "misconception"):
            assert doc.get(k) is not None, f"phase{i} missing {k}"
        assert len(doc["items"]) >= 5


def test_ladder_five_rungs():
    doc = load_yaml("ladder.yaml")
    assert [r["rung"] for r in doc["rungs"]] == [1, 2, 3, 4, 5]
    for r in doc["rungs"]:
        assert r["name"] and r["claude_role"] and r["bloom_levels"] and r["problem_classes"]
