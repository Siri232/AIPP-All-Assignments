from typing import Any

def is_palindrome_copilot(s: Any) -> bool:
    """
    Copilot-style palindrome checker with simple interactive prompt.

    This file provides a concise implementation and a small CLI that asks the
    user for text input, then reports whether it is a palindrome.

    Returns False for non-string inputs.
    Normalizes input by lowercasing and keeping only alphanumeric characters.
    Compares the normalized string to its reverse.

    Example:
        >>> is_palindrome_copilot("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome_copilot("hello")
        False
    """
    if not isinstance(s, str):
        return False
    s = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]


def main() -> None:
    """Simple interactive loop to accept user input and print results."""
    try:
        while True:
            text = input("\nEnter text to check: ")
            if not text:
                print("Goodbye.")
                break

            is_pal = is_palindrome_copilot(text)
            print(f"Result: {'Palindrome' if is_pal else 'Not a palindrome'}\n")
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if _name_ == "_main_":
    main()