# Data Model: Calculator CLI

## Entities

### Expression
- **Type**: String
- **Description**: The mathematical expression entered by the user.
- **Validation Rules**: 
  - MUST contain only numbers, operators (`+`, `-`, `*`, `/`), parentheses, and spaces.
  - MUST be a valid Python arithmetic expression.
  - Division by zero is NOT allowed.

### Result
- **Type**: `decimal.Decimal`
- **Description**: The numerical result of evaluating an expression.
- **Precision**: 10 decimal places.

## State Transitions
1.  **INPUT**: User enters a string in the REPL.
2.  **VALIDATE**: Check for syntax and divide-by-zero errors.
3.  **EVALUATE**: Compute result using `ast` and `decimal`.
4.  **OUTPUT**: Format result to 10 decimal places and display.
5.  **RESET**: Prepare for next input.
