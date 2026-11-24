"""Tests for the refactored tuition fee calculations."""

import pytest

from fees import Course, StudentType, process_all, tuition_fee
from legacy_fees import calc


def legacy_courses(*hours):
    """Create legacy course dictionaries."""
    return [{"h": h} for h in hours]


def courses(*hours):
    """Create Course objects."""
    return [Course(h) for h in hours]


def student(name, kind):
    """Create a student with one three-hour course."""
    return {
        "name": name,
        "type": kind,
        "courses": courses(3),
        "summer": False,
    }


@pytest.mark.parametrize(
    "hours, code, kind, summer",
    [
        ((3, 3, 3), 1, StudentType.REGULAR, False),
        ((3, 3, 3, 3, 3, 3), 1, StudentType.REGULAR, True),
        ((3, 4), 2, StudentType.STAFF_CHILD, False),
        ((3, 3), 3, StudentType.SCHOLARSHIP, True),
    ],
)
def test_same_result_as_legacy(hours, code, kind, summer):
    """Check that refactored results match legacy results."""
    old = calc(
        legacy_courses(*hours),
        code,
        2026,
        summer,
        None,
    )

    new = tuition_fee(courses(*hours), kind, summer)

    assert new == old


def test_large_fee_gets_reduction():
    """Check that large fees receive the reduction."""
    assert tuition_fee(
        courses(6, 6, 6),
        StudentType.REGULAR,
    ) == 6100


def test_scholarship_student_is_not_skipped():
    """Check that scholarship students receive zero fees."""
    students = [
        student("Sara", StudentType.REGULAR),
        student("Omar", StudentType.SCHOLARSHIP),
    ]

    assert process_all(students) == {
        "Sara": 1050,
        "Omar": 0,
    }
