"""Calculate tuition fees for different student types."""

from dataclasses import dataclass
from enum import Enum


@dataclass
class Course:
    """Represent a course and its credit hours."""

    hours: int


class StudentType(Enum):
    """Available student categories."""

    REGULAR = 1
    STAFF_CHILD = 2
    SCHOLARSHIP = 3


HOURLY_RATE = 350
STAFF_DISCOUNT = 0.5
FEE_LIMIT = 6000
FEE_REDUCTION = 200
SUMMER_FEE = 150


def calculate_course_fee(course, student_type):
    """Calculate the fee for one course."""
    if student_type == StudentType.REGULAR:
        return course.hours * HOURLY_RATE

    if student_type == StudentType.STAFF_CHILD:
        return course.hours * HOURLY_RATE * STAFF_DISCOUNT

    return 0


def tuition_fee(courses, student_type, summer=False):
    """Calculate the total tuition fee for a student."""
    total = sum(
        calculate_course_fee(course, student_type)
        for course in courses
    )

    if total > FEE_LIMIT:
        total -= FEE_REDUCTION

    if summer:
        total += SUMMER_FEE

    return total


def process_all(students):
    """Calculate and return fees for all students."""
    results = {}

    for student in students:
        student_type = StudentType(student["type"])

        fee = tuition_fee(
            student["courses"],
            student_type,
            student["summer"],
        )

        results[student["name"]] = fee

    return results
