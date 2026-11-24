# Legacy Fees – Findings

## 1. Hidden Bug in ProcessAll

The `ProcessAll` function contains a hidden bug because it handles only student types 1 and 2, but does not handle scholarship students (type 3).

### Case 1: Scholarship student after a regular student

When Sara (type 1) is processed first, her fee is calculated as 1050. When Omar (type 3) is processed next, the program does not update the `fee` variable. As a result, Omar incorrectly receives Sara's previous fee of 1050 instead of 0.

### Case 2: Scholarship student processed first

When Omar (type 3) is processed alone, the `fee` variable has never been assigned. Python raises an `UnboundLocalError`.

### Root Cause

The function uses two independent `if` statements and does not include a case for scholarship students (type 3). The previous value of `fee` may be reused accidentally.

### Expected Behavior

Scholarship students should have a fee of 0.

## 2. Ruff Findings Table

Command: `ruff check legacy_fees.py`

| Issue | Description |
|---|---|
| F401 | Unused imports: os and math |
| C901 | calc function is too complex |
| PLR0913 | Too many function arguments |
| PLR0917 | Too many positional arguments |
| ARG001 | Unused argument y |
| B006 | Mutable default argument `extra=[]` |
| PLR2004 | Magic numbers used in comparisons |
| E712 | Incorrect comparison with True |
| E711 | Incorrect comparison with None |
| F841 | Unused variable tmp |
| N802 | ProcessAll does not follow snake_case naming |

Total: 17 Ruff errors.

## 3. Pylint Findings

Command: `python -m pylint legacy_fees.py`

- Missing module and function docstrings.
- Dangerous mutable default argument.
- Too many function arguments.
- Incorrect comparisons with True and None.
- Unused argument y.
- Unused variable tmp.
- Function name ProcessAll does not follow snake_case.
- Possible use of variable fee before assignment.
- Unused imports os and math.

Pylint Score: 4.86/10.

## 4. Additional Code Smells

1. **Long and complex function:** The `calc` function handles multiple responsibilities, making it difficult to understand and maintain.

2. **Magic numbers:** Values such as 350, 6000, 200, and 150 are written directly in the code instead of being defined as named constants.

3. **Poor naming:** Short names such as `d`, `t`, `y`, `s`, and `disc` make the code difficult to understand.

4. **Duplicate conditional logic:** Similar student-type checks are repeated in different functions.

5. **Unused code:** The imports `os` and `math`, and the variable `tmp`, are unnecessary.

## 5. Conclusion

The legacy code contains readability, maintainability, and reliability problems. The most serious issue is the hidden scholarship student bug in `ProcessAll`, which can produce an incorrect fee or raise an UnboundLocalError.