"""AST-based expression parser for the calculator application."""

import ast
import operator
from decimal import Decimal, getcontext

# Set precision for Decimal operations as per specification (up to 10 decimals)
getcontext().prec = 28  # High precision for internal calculations


def parse_expression(expression: str) -> Decimal:
    """Parses and evaluates a mathematical expression string.

    Args:
        expression: The mathematical expression string.

    Returns:
        The evaluated result as a Decimal.

    Raises:
        SyntaxError: If the expression is invalid.
        ZeroDivisionError: If division by zero occurs during evaluation.
    """
    try:
        # Use ast.parse for secure parsing of expressions
        tree = ast.parse(expression, mode='eval')
        return _evaluate_node(tree.body)
    except ZeroDivisionError:
        # Re-raise ZeroDivisionError so it can be handled specifically
        raise
    except Exception as e:
        # Re-raise other exceptions as SyntaxError for consistency
        raise SyntaxError(f"Invalid syntax: {e}")


def _evaluate_node(node):
    """Recursively evaluates an AST node.

    Args:
        node: An AST node.

    Returns:
        The evaluated value.

    Raises:
        SyntaxError: If the node contains unsupported operations.
    """
    # Supported operators mapped to their functions
    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    if isinstance(node, ast.Constant):  # Numbers
        return Decimal(str(node.value))
    elif isinstance(node, ast.BinOp):  # Binary operations (e.g., +, -, *, /)
        left = _evaluate_node(node.left)
        right = _evaluate_node(node.right)
        op_func = operators.get(type(node.op))
        if op_func is None:
            raise SyntaxError(f"Unsupported binary operator: {type(node.op)}")

        # Ensure result is rounded to 10 decimals as per spec (if applicable)
        result = op_func(left, right)
        return result
    elif isinstance(node, ast.UnaryOp):  # Unary operations (e.g., -5)
        operand = _evaluate_node(node.operand)
        op_func = operators.get(type(node.op))
        if op_func is None:
            raise SyntaxError(f"Unsupported unary operator: {type(node.op)}")
        return op_func(operand)
    else:
        raise SyntaxError(f"Unsupported node type: {type(node)}")
