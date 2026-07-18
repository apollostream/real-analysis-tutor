"""Theorem Ledger V2.1 and Error Log engine.

Stdlib-only persistence for two append-only JSON logs kept in a
learner's workspace directory:

- ``ledger.json``    -- list of theorem-ledger entries (see LEDGER_FIELDS).
- ``error_log.json`` -- list of error-log entries (see ERROR_CATEGORIES).

Both files are written atomically (write to a temp file, then
``os.replace``) so a crash mid-write never corrupts the log.
"""

import json
import os
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path

LEDGER_FIELDS = [
    "theorem",
    "statement",
    "proof_idea",
    "load_bearing_hypothesis",
    "counterexample_if_removed",
    "converse_true",
    "converse_example",
    "misconception",
    "misconception_refutation",
    "depends_on",
    "downstream",
    "analogues",
    "lean_status",
    "bloom_level",
]

ERROR_CATEGORIES = [
    "quantifier_error",
    "missing_hypothesis",
    "invalid_inference",
    "wrong_theorem",
    "delta_depends_on_x",
    "converse_confusion",
]


def _load_json_list(path: Path) -> list:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text())
    except json.JSONDecodeError:
        return []
    return data if isinstance(data, list) else []


def _append_json_list(path: Path, item: dict) -> None:
    """Atomically append ``item`` to the JSON list stored at ``path``."""
    items = _load_json_list(path)
    items.append(item)
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(json.dumps(items, indent=2))
    os.replace(tmp_path, path)


def load_ledger(workspace: Path) -> list:
    """Return the list of theorem-ledger entries for ``workspace``."""
    return _load_json_list(Path(workspace) / "ledger.json")


def append_theorem(workspace: Path, entry: dict) -> None:
    """Validate and append a theorem entry to ``ledger.json``.

    Raises ValueError naming every LEDGER_FIELDS name missing from
    ``entry``. On success, stamps the entry with an "added" ISO date
    and appends it atomically.
    """
    missing = [f for f in LEDGER_FIELDS if f not in entry]
    if missing:
        raise ValueError(f"Missing required ledger field(s): {', '.join(missing)}")
    record = dict(entry)
    record["added"] = date.today().isoformat()
    _append_json_list(Path(workspace) / "ledger.json", record)


def append_error(workspace: Path, category: str, description: str, context: str = "") -> None:
    """Validate and append an error-log entry to ``error_log.json``."""
    if category not in ERROR_CATEGORIES:
        raise ValueError(
            f"Invalid error category: {category!r}; must be one of {ERROR_CATEGORIES}"
        )
    record = {
        "date": datetime.now(timezone.utc).isoformat(),
        "category": category,
        "description": description,
        "context": context,
    }
    _append_json_list(Path(workspace) / "error_log.json", record)


def error_counts(workspace: Path, last_n: int = 20) -> dict:
    """Return category counts over the most recent ``last_n`` error entries."""
    entries = _load_json_list(Path(workspace) / "error_log.json")
    recent = entries[-last_n:] if last_n else entries
    return dict(Counter(e["category"] for e in recent))
