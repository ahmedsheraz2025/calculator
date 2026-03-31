# Calculator CLI

A robust, PEP 8 compliant Python CLI calculator that supports basic arithmetic with standard operator precedence (PEMDAS) and high precision.

## Features

- **Basic Arithmetic**: Support for `+`, `-`, `*`, and `/`.
- **Precedence**: Correct handling of operator precedence (e.g., `5 + 3 * 2 = 11`).
- **High Precision**: Uses `decimal` for accurate calculations with up to 10 decimal places.
- **Dynamic Formatting**: Results are shown as integers for whole numbers and fractions only when necessary.
- **Error Handling**: Graceful handling of division by zero and syntax errors.
- **Interactive REPL**: Simple and easy-to-use terminal interface.

## Installation

This project uses `uv` for dependency management.

1. Ensure you have `uv` installed.
2. Clone the repository.
3. Run `uv sync` to install dependencies and set up the environment.

## Usage

Start the interactive calculator:

```bash
uv run src/main.py
```

### Examples

```text
calc > 5 + 3
8
calc > 1 / 3
0.3333333333
calc > (10 + 2) * 3
36
```

### Commands

- `clear`: Clears the terminal screen.
- `exit` or `quit`: Exits the calculator.

## Testing

Run the test suite using `pytest`:

```bash
uv run pytest
```

## Linting

Check code quality with `ruff`:

```bash
uv run ruff check src tests
```

## Technical Stack

- **Language**: Python 3.12+
- **Precision**: Standard Library `decimal` module
- **Parsing**: Standard Library `ast` module
- **Environment Management**: `uv`
- **Testing**: `pytest`
- **Linting**: `ruff`
