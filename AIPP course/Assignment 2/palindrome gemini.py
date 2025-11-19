# palindrome_compare.py
# Gemini-style palindrome checker with CLI input prompt

import re
from typing import Tuple


def gemini_palindrome(s: str) -> Tuple[bool, str]:
    """
    Gemini-style palindrome check.

    - Normalizes the input by removing all non-alphanumeric characters and lowercasing.
    - Returns a tuple (is_palindrome, normalized_string).

    Args:
        s: input string to check

    Returns:
        (True/False, normalized string used for the check)
    """
    if s is None:
        return False, ""
    # Remove non-alphanumeric characters and lowercase
    cleaned = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    return (cleaned == cleaned[::-1]), cleaned


if __name__ == "__main__":
    print("Gemini-style Palindrome Checker")
    print("Enter a phrase to check. Press Enter on an empty line to exit.")
    try:
        while True:
            user_input = input("Input> ").strip()
            if user_input == "":
                print("Exiting.")
                break
            is_pal, normalized = gemini_palindrome(user_input)
            if normalized == "":
                print("No alphanumeric characters found in input.")
            else:
                print(f"Normalized: {normalized}")
                print("Result: Palindrome" if is_pal else "Result: Not a palindrome")
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
