"""Simple calculator: library functions plus an interactive CLI."""
import sys


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculate(a, op, b):
    if op not in OPERATIONS:
        raise ValueError(f"Unknown operator: {op!r}")
    return OPERATIONS[op](a, b)


def main():
    if len(sys.argv) == 4:
        try:
            print(calculate(float(sys.argv[1]), sys.argv[2], float(sys.argv[3])))
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
            sys.exit(1)
        return

    print("Calculator - enter e.g. '3 + 4' (or 'q' to quit)")
    while True:
        line = input("> ").strip()
        if line.lower() in ("q", "quit", "exit"):
            break
        parts = line.split()
        if len(parts) != 3:
            print("Format: <number> <operator> <number>")
            continue
        try:
            print(calculate(float(parts[0]), parts[1], float(parts[2])))
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
