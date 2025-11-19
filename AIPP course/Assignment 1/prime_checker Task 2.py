# prime_checker.py
"""
Simple interactive prime number checker.

Usage:
    python prime_checker.py

Enter an integer to check if it's prime, or 'q' to quit.
"""

import math
import sys


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise.

    Uses a simple deterministic algorithm suitable for integers up to at least
    2**31-1. Handles n < 2 as non-prime.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    # test odd divisors up to sqrt(n)
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def main() -> None:
    print("Prime checker. Enter an integer to check, or 'q' to quit.")
    while True:
        try:
            s = input("Enter integer (or 'q' to quit): ").strip()
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye!')
            return

        if s.lower() in {'q', 'quit', 'exit'}:
            print('Goodbye!')
            return

        if not s:
            print('No input provided; please enter an integer or q to quit.')
            continue

        # allow leading + or - signs
        try:
            n = int(s)
        except ValueError:
            print("Invalid input. Please enter a whole integer (e.g. 17, -5).")
            continue

        if is_prime(n):
            print(f"{n} is prime.")
        else:
            print(f"{n} is not prime.")


if __name__ == '__main__':
    main()
