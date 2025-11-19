# reverse_string.py
"""
Interactive reverse-string checker.

Usage:
    python reverse_string.py

Enter any text and the program will print its reversal. Enter 'q' to quit.
"""

# Function to reverse a string
def reverse_string(s: str) -> str:
    """Return the reverse of the input string s.

    This function is intentionally simple so Copilot-style completion would
    typically generate the slicing-based implementation below.
    """
    return s[::-1]


def main() -> None:
    print("Reverse-string tool. Enter text to reverse, or 'q' to quit.")
    while True:
        try:
            s = input("Enter text (or 'q' to quit): ").rstrip('\n')
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye!')
            return

        if not s:
            print('No input provided; please type something or q to quit.')
            continue

        if s.lower() in {'q', 'quit', 'exit'}:
            print('Goodbye!')
            return

        reversed_s = reverse_string(s)
        print(f"Reversed: {reversed_s}")


if __name__ == '__main__':
    main()
