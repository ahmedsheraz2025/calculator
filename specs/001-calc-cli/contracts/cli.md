# CLI Contract: Calculator

## Interactive REPL

### Commands
- **exit**: Close the calculator.
- **quit**: Close the calculator.
- **clear**: Clear the screen (optional, if possible).
- **help**: Show usage instructions.

### Inputs
- **Expression**: A mathematical string (e.g., `2 + 3 * 4`).

### Expected Outputs
- **Success**: A numeric value formatted dynamically (integer for whole numbers, up to 10 decimal places only as needed for fractions).
- **Syntax Error**: `Error: Invalid syntax`
- **Math Error**: `Error: Division by zero`
- **Unknown Error**: `Error: [Message]`

### Examples
- **Input**: `5 + 3`
- **Output**: `8`
- **Input**: `1 / 3`
- **Output**: `0.3333333333`
- **Input**: `1.5 + 1.5`
- **Output**: `3`
- **Input**: `10 / 0`
- **Output**: `Error: Division by zero`
- **Input**: `5 ++ 3`
- **Output**: `Error: Invalid syntax`
