"""Integration tests for the calculator CLI."""

import subprocess
import sys


def run_calc(inputs):
    """Simulates running the calculator with the given inputs."""
    process = subprocess.Popen(
        [sys.executable, "src/main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env={"PYTHONPATH": "src"}
    )

    stdout, stderr = process.communicate(input="\n".join(inputs))
    return stdout, stderr


def test_cli_arithmetic():
    """Test standard arithmetic in the CLI."""
    stdout, _ = run_calc(["5 + 3", "exit"])
    assert "8" in stdout

    stdout, _ = run_calc(["1 / 3", "exit"])
    assert "0.3333333333" in stdout


def test_cli_error_handling():
    """Test error messages in the CLI."""
    stdout, _ = run_calc(["10 / 0", "exit"])
    assert "Error: Division by zero" in stdout

    stdout, _ = run_calc(["5 +* 3", "exit"])
    assert "Error: Invalid syntax" in stdout

def test_cli_exit_commands():
    """Test exit and quit commands."""
    stdout, _ = run_calc(["exit"])
    assert "Goodbye!" in stdout

    stdout, _ = run_calc(["quit"])
    assert "Goodbye!" in stdout
