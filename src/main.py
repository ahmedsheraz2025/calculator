"""Interactive REPL loop for the calculator application."""

import os

from calculator.evaluator import format_result
from calculator.parser import parse_expression


def main():
    """Main entry point for the calculator application."""
    print("Welcome to the Calculator CLI!")
    print("Type your expressions (e.g., 5 + 3) and press Enter.")
    print("Commands: 'exit', 'quit', 'clear'")

    while True:
        try:
            # Display prompt and wait for input
            user_input = input("calc > ").strip().lower()

            # Handle empty input
            if not user_input:
                continue

            # Handle exit commands
            if user_input in ("exit", "quit"):
                print("Goodbye!")
                break

            # Handle clear command
            if user_input == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')
                continue

            # Parse and evaluate the expression
            result = parse_expression(user_input)

            # Format and display the result
            print(format_result(result))

        except ZeroDivisionError:
            print("Error: Division by zero")
        except SyntaxError as e:
            # Handle user-friendly error messages as per specs
            if "division by zero" in str(e).lower():
                print("Error: Division by zero")
            else:
                print("Error: Invalid syntax")
        except EOFError:
            # Handle Ctrl+D gracefully
            print("\nGoodbye!")
            break
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\nGoodbye!")
            break
        except Exception:
            # Catch-all for unexpected errors
            print("Error: Invalid syntax")


if __name__ == "__main__":
    main()
