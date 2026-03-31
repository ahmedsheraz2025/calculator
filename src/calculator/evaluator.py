"""Arithmetic evaluator for the calculator application."""

from decimal import ROUND_HALF_UP, Decimal, getcontext

# Ensure precision for high-level operations
getcontext().prec = 28


def evaluate_expression(left: Decimal, right: Decimal, op: str) -> Decimal:
    """Evaluates a basic arithmetic operation.

    Args:
        left: The left operand.
        right: The right operand.
        op: The operator as a string.

    Returns:
        The result as a Decimal.

    Raises:
        ZeroDivisionError: If right is zero for division.
        ValueError: If the operator is unsupported.
    """
    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    elif op == '*':
        return left * right
    elif op == '/':
        if right == 0:
            raise ZeroDivisionError("Division by zero")
        return left / right
    else:
        raise ValueError(f"Unsupported operator: {op}")


def format_result(value: Decimal) -> str:
    """Formats the result according to precision rules.

    - Whole numbers are integers (e.g., 8.0 -> "8").
    - Up to 10 decimal places for fractions (e.g., 1/3 -> "0.3333333333").

    Args:
        value: The result to format.

    Returns:
        A formatted string representing the value.
    """
    # Truncate to 10 decimal places as per specification
    formatted = value.quantize(Decimal('1e-10'), rounding=ROUND_HALF_UP).normalize()

    # Check if result is functionally an integer
    if formatted == formatted.to_integral_value():
        return f"{formatted:g}"

    # Return normalized scientific-free string representation
    return f"{formatted:f}"
