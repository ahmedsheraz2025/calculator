"""Unit tests for the expression parser."""

from decimal import Decimal

import pytest

from calculator.parser import parse_expression


def test_parse_simple_expression():
    """Test parsing simple arithmetic expressions."""
    assert parse_expression("5 + 3") == Decimal("8")
    assert parse_expression("10 - 4") == Decimal("6")
    assert parse_expression("6 * 7") == Decimal("42")
    assert parse_expression("20 / 4") == Decimal("5")


def test_parse_precedence():
    """Test parsing with operator precedence (PEMDAS)."""
    assert parse_expression("5 + 3 * 2") == Decimal("11")
    assert parse_expression("(5 + 3) * 2") == Decimal("16")
    assert parse_expression("10 / 2 + 3") == Decimal("8")


def test_parse_decimals():
    """Test parsing expressions with decimal numbers."""
    assert parse_expression("1.5 + 1.5") == Decimal("3.0")
    assert parse_expression("1 / 3") == Decimal("0.3333333333333333333333333333")


def test_parse_negative_numbers():
    """Test parsing expressions with negative numbers."""
    assert parse_expression("-5 + 3") == Decimal("-2")
    assert parse_expression("10 * -2") == Decimal("-20")


def test_parse_invalid_syntax():
    """Test parsing invalid syntax expressions."""
    # We catch generic Exception and raise SyntaxError in parser.py
    with pytest.raises(SyntaxError, match="Invalid syntax"):
        parse_expression("5 +* 3")
    with pytest.raises(SyntaxError, match="Invalid syntax"):
        parse_expression("abc")
    with pytest.raises(SyntaxError, match="Invalid syntax"):
        parse_expression("5 +")
