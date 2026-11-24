
"""Convert a numeric score into a letter grade."""

MIN_SCORE = 0
MAX_SCORE = 100

GRADE_A = 90
GRADE_B = 80
GRADE_C = 70
GRADE_D = 60


def validate_score(score):
    """Check that the score is within the allowed range."""
    if score < MIN_SCORE or score > MAX_SCORE:
        raise ValueError("Score must be between 0 and 100")


def letter_grade(score):
    """Return the letter grade for a valid score."""
    validate_score(score)

    if score >= GRADE_A:
        return "A"

    if score >= GRADE_B:
        return "B"

    if score >= GRADE_C:
        return "C"

    if score >= GRADE_D:
        return "D"

    return "F"
