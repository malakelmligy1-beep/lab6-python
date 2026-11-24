# Week 5 – After Refactoring Report

## 1. Refactored Files

- `fees.py`: Replaced the legacy fee calculation with structured classes and functions.
- `test_fees.py`: Added characterization tests to verify the refactored behavior.

## 2. Improvements

- Replaced magic numbers with named constants.
- Split complex fee calculation into smaller functions.
- Used `Course` dataclass to represent courses.
- Used `StudentType` Enum to represent student categories.
- Fixed the scholarship student bug.
- Removed the mutable default argument.
- Added meaningful docstrings.
- Improved readability and maintainability.

## 3. Testing Results

Command: `pytest -v test_fees.py`

Result: 6 tests passed.

## 4. Ruff Results

Command: `ruff check fees.py test_fees.py`

Result: All checks passed!

## 5. Pylint Results

| File | Score |
|---|---:|
| fees.py | 10.00/10 |
| test_fees.py | 10.00/10 |

## 6. Before and After Comparison

Before refactoring:
- Complex fee calculation function.
- Magic numbers.
- Mutable default argument.
- Missing documentation.
- Scholarship bug in ProcessAll.
- Pylint score for legacy_fees.py: 4.86/10.

After refactoring:
- Smaller and clearer functions.
- Named constants.
- Structured data using dataclass and Enum.
- All 6 tests passed.
- Ruff reported no issues.
- Both refactored files scored 10/10 in Pylint.

## 7. Conclusion

The refactoring improved code readability, maintainability, and code quality while preserving the expected fee calculation behavior. The scholarship student bug was also fixed.

## 8. Pair Programming Reflection

Mai helped me during this assignment by discussing the tasks and supporting me while working through the solutions. Her help made it easier to understand the requirements and complete the work.