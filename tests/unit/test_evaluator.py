"""Unit tests for the arithmetic evaluator."""

from decimal import Decimal

import pytest

from calculator.evaluator import evaluate_expression, format_result


def test_evaluate_basic_arithmetic():
    """Test basic arithmetic operations."""
    assert evaluate_expression(Decimal("5"), Decimal("3"), "+") == Decimal("8")
    assert evaluate_expression(Decimal("10"), Decimal("4"), "-") == Decimal("6")
    assert evaluate_expression(Decimal("6"), Decimal("7"), "*") == Decimal("42")
    assert evaluate_expression(Decimal("20"), Decimal("4"), "/") == Decimal("5")


def test_evaluate_decimal_arithmetic():
    """Test arithmetic operations with decimals."""
    assert (
        evaluate_expression(Decimal("1.5"), Decimal("1.5"), "+") == Decimal("3.0")
    )
    # Match context precision (28 decimals)
    assert (
        evaluate_expression(Decimal("1"), Decimal("3"), "/") == Decimal("0.3333333333333333333333333333")
    )


def test_evaluate_division_by_zero():
    """Test division by zero error."""
    with pytest.raises(ZeroDivisionError, match="Division by zero"):
        evaluate_expression(Decimal("10"), Decimal("0"), "/")


def test_format_result():
    """Test dynamic result formatting."""
    assert format_result(Decimal("8.0")) == "8"
    assert format_result(Decimal("0.3333333333")) == "0.3333333333"
    assert format_result(Decimal("5")) == "5"
    # Truncated to 10 decimals
    assert format_result(Decimal("1.234567890123")) == "1.2345678901"
