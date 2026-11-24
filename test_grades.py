
"""Tests for the letter grade function."""

import pytest

from grades import letter_grade


def test_ninety_is_an_a():
    """Check that 90 returns A."""
    assert letter_grade(90) == "A"


def test_eighty_nine_is_a_b():
    """Check that 89 returns B."""
    assert letter_grade(89) == "B"


def test_below_sixty_fails():
    """Check that a score below 60 returns F."""
    assert letter_grade(59) == "F"


def test_score_above_100_is_rejected():
    """Check that scores above 100 raise a ValueError."""
    with pytest.raises(ValueError):
        letter_grade(101)


def test_zero_is_f():
    """Check that zero returns F."""
    assert letter_grade(0) == "F"


def test_hundred_is_a():
    """Check that 100 returns A."""
    assert letter_grade(100) == "A"


def test_sixty_is_d():
    """Check that 60 returns D."""
    assert letter_grade(60) == "D"


def test_sixty_nine_is_d():
    """Check that 69 returns D."""
    assert letter_grade(69) == "D"


def test_seventy_is_c():
    """Check that 70 returns C."""
    assert letter_grade(70) == "C"


def test_negative_score_is_rejected():
    """Check that negative scores raise a ValueError."""
    with pytest.raises(ValueError):
        letter_grade(-1)
