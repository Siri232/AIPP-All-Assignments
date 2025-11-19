# largest_in_list.py
"""
Interactive tool: find the largest number in a list.

Usage:
    python largest_in_list.py

Enter numbers separated by commas or spaces (e.g. "1, 3, 2" or "1 3 2").
Enter 'q' to quit.
"""

from typing import List, Union, Optional

# Function to find the largest number in a list
# (Copilot-style completion would often produce a simple loop like below)

def largest_manual(nums: List[Union[int, float]]) -> Union[int, float]:
    """Return the largest number in nums using an explicit loop.

    Raises ValueError if nums is empty.
    Time complexity: O(n), Space: O(1).
    """
    if not nums:
        raise ValueError("empty list")
    largest = nums[0]
    for x in nums[1:]:
        if x > largest:
            largest = x
    return largest


def largest_builtin(nums: List[Union[int, float]]) -> Union[int, float]:
    """Return the largest number using Python's built-in max().

    This is implemented in C and will generally be faster than a pure-Python
    loop for large lists, though both are O(n) time.
    """
    if not nums:
        raise ValueError("empty list")
    return max(nums)


def parse_numbers(s: str) -> Optional[List[float]]:
    """Parse a user input string into a list of numbers (floats).

    Accepts comma- or whitespace-separated numbers. Returns None for invalid input.
    """
    if not s:
        return None

    # allow both comma and whitespace separators
    parts = [p for chunk in s.split(',') for p in chunk.split()]
    nums: List[float] = []
    for p in parts:
        if p == '':
            continue
        try:
            # parse as float to accept both integers and floats
            n = float(p)
            nums.append(n)
        except ValueError:
            return None
    return nums


def main() -> None:
    print("Largest-in-list tool. Enter numbers separated by commas or spaces, or 'q' to quit.")
    while True:
        try:
            s = input("Enter numbers (or 'q' to quit): ").strip()
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye!')
            return

        if not s:
            print('No input provided; please enter some numbers or q to quit.')
            continue

        if s.lower() in {'q', 'quit', 'exit'}:
            print('Goodbye!')
            return

        nums = parse_numbers(s)
        if nums is None:
            print("Invalid input. Please enter numbers separated by commas or spaces (e.g. '1, 2, 3' or '1 2 3').")
            continue

        if len(nums) == 0:
            print('No numbers parsed; try again.')
            continue

        try:
            a = largest_manual(nums)
            b = largest_builtin(nums)
        except ValueError as exc:
            print(str(exc))
            continue

        # Both should agree; show both for demonstration / testing
        print(f"Largest (manual)  = {a}")
        print(f"Largest (builtin) = {b}")


if __name__ == '__main__':
    main()
