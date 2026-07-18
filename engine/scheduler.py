"""SM-2 spaced-repetition scheduler.

Interval math ALWAYS lives here — never delegated to the model. Callers
(the tutor) only supply a 0-5 grade for a review; this module owns the
resulting repetition count, ease factor, and due date.
"""

import datetime
import json
import os
from pathlib import Path

REVIEWS_FILE = "reviews.json"

DEFAULT_EF = 2.5
EF_FLOOR = 1.3


def _new_item(concept: str) -> dict:
    return {
        "concept": concept,
        "ef": DEFAULT_EF,
        "reps": 0,
        "interval": 0,
        "due": None,
        "last_grade": None,
    }


def record_review(reviews: list, concept: str, grade: int, today: datetime.date) -> list:
    """Apply SM-2 to `concept` for `grade` (0-5) on `today`.

    Returns a new list of review items (the input list's items are not
    mutated in place; matching items are replaced, new ones appended).
    """
    if not isinstance(grade, int) or isinstance(grade, bool) or not (0 <= grade <= 5):
        raise ValueError(f"grade must be an int 0-5, got {grade!r}")

    reviews = list(reviews)
    idx = None
    item = None
    for i, r in enumerate(reviews):
        if r.get("concept") == concept:
            idx = i
            item = dict(r)
            break
    if item is None:
        item = _new_item(concept)

    old_ef = item["ef"]

    if grade < 3:
        reps = 0
        interval = 1
    else:
        reps = item["reps"] + 1
        if reps == 1:
            interval = 1
        elif reps == 2:
            interval = 6
        else:
            interval = round(item["interval"] * old_ef)

    new_ef = max(EF_FLOOR, old_ef + 0.1 - (5 - grade) * (0.08 + (5 - grade) * 0.02))

    item["ef"] = new_ef
    item["reps"] = reps
    item["interval"] = interval
    item["due"] = (today + datetime.timedelta(days=interval)).isoformat()
    item["last_grade"] = grade

    if idx is None:
        reviews.append(item)
    else:
        reviews[idx] = item

    return reviews


def due(reviews: list, today: datetime.date) -> list:
    """Concepts whose due date is on or before `today`, oldest first."""
    items = [r for r in reviews if datetime.date.fromisoformat(r["due"]) <= today]
    items.sort(key=lambda r: r["due"])
    return [r["concept"] for r in items]


def load_reviews(workspace: Path) -> list:
    path = Path(workspace) / REVIEWS_FILE
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return []


def save_reviews(workspace: Path, reviews: list) -> None:
    workspace = Path(workspace)
    path = workspace / REVIEWS_FILE
    tmp_path = workspace / (REVIEWS_FILE + ".tmp")
    tmp_path.write_text(json.dumps(reviews, indent=2))
    os.replace(tmp_path, path)
