import pytest
from engine import ledger


def full_entry():
    return {f: ("planned" if f == "lean_status" else "x") for f in ledger.LEDGER_FIELDS}


def test_fields_and_categories_exact():
    assert ledger.LEDGER_FIELDS[0] == "theorem" and len(ledger.LEDGER_FIELDS) == 14
    assert "misconception_refutation" in ledger.LEDGER_FIELDS
    assert set(ledger.ERROR_CATEGORIES) == {
        "quantifier_error", "missing_hypothesis", "invalid_inference",
        "wrong_theorem", "delta_depends_on_x", "converse_confusion"}


def test_append_theorem_and_load(tmp_path):
    ledger.append_theorem(tmp_path, full_entry())
    entries = ledger.load_ledger(tmp_path)
    assert len(entries) == 1 and entries[0]["theorem"] == "x" and "added" in entries[0]


def test_missing_field_rejected(tmp_path):
    e = full_entry(); del e["misconception"]
    with pytest.raises(ValueError, match="misconception"):
        ledger.append_theorem(tmp_path, e)


def test_bad_category_rejected(tmp_path):
    with pytest.raises(ValueError):
        ledger.append_error(tmp_path, "sloppy", "oops")


def test_error_counts_last_n(tmp_path):
    for _ in range(3):
        ledger.append_error(tmp_path, "quantifier_error", "d")
    ledger.append_error(tmp_path, "converse_confusion", "d")
    c = ledger.error_counts(tmp_path, last_n=2)
    assert c == {"quantifier_error": 1, "converse_confusion": 1}
