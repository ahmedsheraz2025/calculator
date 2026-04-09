# Research: Calculator CLI Implementation (Python)

## Decision: Expression Parsing
**Chosen**: `ast.parse` and a custom AST walker.
**Rationale**: `ast.parse` is part of the Python standard library and provides a robust, built-in parser that naturally handles operator precedence (PEMDAS) and basic syntax errors. It is safer than `eval()` as we can explicitly whitelist only allowed nodes (`BinOp`, `UnaryOp`, `Num`, `Constant`).
**Alternatives considered**: 
- `eval()`: Rejected due to security risks.
- `shunting-yard`: Rejected to minimize custom parsing logic when a robust standard parser exists.
- `ast.literal_eval`: Rejected because it does not support arithmetic operations directly.

## Decision: Precision Management
**Chosen**: `decimal.Decimal`.
**Rationale**: Python's `float` uses IEEE 754 binary floating-point representation, which can lead to precision errors (e.g., `0.1 + 0.2 != 0.3`). The `decimal` module provides support for fast correctly-rounded decimal floating-point arithmetic, which is required for the 10-decimal-place accuracy.
**Alternatives considered**:
- `float` and `round()`: Rejected due to potential representation issues.

## Decision: REPL Loop
**Chosen**: Standard `while True` with `input()`.
**Rationale**: Simple, effective, and requires no external dependencies. Complemented by `try-except` blocks to satisfy robustness requirements.
**Alternatives considered**:
- `cmd` module: Rejected as it might be overkill for a simple single-line calculator.

## Decision: Project Structure
**Chosen**: Single project with `src/` and `tests/`.
**Rationale**: Standard Python project layout.
