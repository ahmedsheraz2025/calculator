---
id: 0014
title: Fix result formatting to avoid scientific notation
stage: green
date_iso: 2026-04-01
surface: agent
model: gemini-2.0-flash-exp
feature: 001-calc-cli
branch: main
user: current
command: none
labels: ["bugfix", "formatting", "decimal"]
links:
  spec: "specs/001-calc-cli/spec.md"
  ticket: null
  adr: null
  pr: null
files_yaml:
  - src/calculator/evaluator.py
  - tests/unit/test_evaluator.py
tests_yaml:
  - tests/unit/test_evaluator.py
---

# Outcome / Evaluation

The formatting issue where `10+10` resulted in `2e+1` was fixed by replacing the `:g` format specifier with `:f` in `format_result`. Additionally, the precision was corrected to strictly adhere to the "up to 10 decimal places" requirement (FR-003) by quantizing with `Decimal('1.0000000000')` before normalization.

# Prompt Text

when i run the project and query 10+10 it prints 2e+1 instead of prints 20, fix it

# Response Text

I have fixed the issue where the calculator would display results like `10+10` in scientific notation (`2e+1`). 

The `format_result` function in `src/calculator/evaluator.py` was updated to:
1. Use `Decimal('1.0000000000')` for quantization to ensure a maximum of 10 decimal places as per specification FR-003.
2. Use the `:f` format specifier instead of `:g` to prevent switching to scientific notation for whole numbers and simple decimals.

Verified the fix with a reproduction script and added a new test case to `tests/unit/test_evaluator.py`. All tests passed.
