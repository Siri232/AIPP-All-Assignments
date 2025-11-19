# factorial.py
"""
Interactive factorial tool with recursive and iterative implementations.

Usage:
    python factorial.py

Enter a non-negative integer to compute its factorial, or 'q' to quit.
"""

from typing import Optional


# Recursive factorial implementation
# Function to compute factorial recursively
def factorial_recursive(n: int) -> int:
    """Return n! computed using recursion.

    Raises ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("factorial is not defined for negative integers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Iterative factorial implementation
# Function to compute factorial iteratively
def factorial_iterative(n: int) -> int:
    """Return n! computed using an iterative loop.

    Raises ValueError for negative inputs.
    """
    if n < 0:
        raise ValueError("factorial is not defined for negative integers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def parse_int(s: str) -> Optional[int]:
    """Try to parse s as int, return int or None if invalid."""
    try:
        return int(s)
    except ValueError:
        return None


def main() -> None:
    print("Factorial tool. Enter a non-negative integer to compute its factorial, or 'q' to quit.")
    while True:
        try:
            s = input("Enter integer (or 'q' to quit): ").strip()
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye!')
            return

        if not s:
            print('No input provided; please enter a whole non-negative integer or q to quit.')
            continue

        if s.lower() in {'q', 'quit', 'exit'}:
            print('Goodbye!')
            return

        n = parse_int(s)
        if n is None:
            print("Invalid input. Please enter a whole integer (e.g. 0, 5, 10).")
            continue

        if n < 0:
            print("Please enter a non-negative integer (n >= 0).")
            continue

        # compute both ways
        try:
            rec = factorial_recursive(n)
            itr = factorial_iterative(n)
        except RecursionError:
            print("Recursive implementation hit recursion limit for this input; try the iterative version or a smaller number.")
            itr = factorial_iterative(n)
            print(f"Iterative: {n}! = {itr}")
            continue

        # sanity check
        if rec != itr:
            print("Warning: recursive and iterative results differ (unexpected).")

        print(f"{n}! (recursive) = {rec}")
        print(f"{n}! (iterative) = {itr}")


if __name__ == '__main__':
    main()
