import datetime
import pytest
from engine import scheduler

D0 = datetime.date(2026, 7, 17)


def test_new_concept_good_grade():
    r = scheduler.record_review([], "sup_inf", 5, D0)
    assert r[0]["interval"] == 1 and r[0]["due"] == "2026-07-18" and r[0]["reps"] == 1


def test_second_review_interval_six():
    r = scheduler.record_review([], "sup_inf", 5, D0)
    r = scheduler.record_review(r, "sup_inf", 5, D0 + datetime.timedelta(days=1))
    assert r[0]["interval"] == 6


def test_third_review_uses_ef():
    r = scheduler.record_review([], "c", 5, D0)
    r = scheduler.record_review(r, "c", 5, D0)
    ef = r[0]["ef"]
    r = scheduler.record_review(r, "c", 5, D0)
    assert r[0]["interval"] == round(6 * ef)


def test_lapse_resets():
    r = scheduler.record_review([], "c", 5, D0)
    r = scheduler.record_review(r, "c", 5, D0)
    r = scheduler.record_review(r, "c", 1, D0)
    assert r[0]["reps"] == 0 and r[0]["interval"] == 1


def test_ef_floor():
    r = []
    for _ in range(10):
        r = scheduler.record_review(r, "c", 0, D0)
    assert r[0]["ef"] == pytest.approx(1.3)


def test_bad_grade_raises():
    with pytest.raises(ValueError):
        scheduler.record_review([], "c", 6, D0)


def test_due_sorted_oldest_first():
    r = [
        {"concept": "b", "ef": 2.5, "reps": 1, "interval": 1, "due": "2026-07-10", "last_grade": 4},
        {"concept": "a", "ef": 2.5, "reps": 1, "interval": 1, "due": "2026-07-01", "last_grade": 4},
        {"concept": "c", "ef": 2.5, "reps": 1, "interval": 1, "due": "2026-08-01", "last_grade": 4},
    ]
    assert scheduler.due(r, D0) == ["a", "b"]
