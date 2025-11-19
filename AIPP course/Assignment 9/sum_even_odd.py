def sum_even_odd(numbers):
    """
    Calculate the sum of even and odd numbers in a list.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        tuple: A tuple containing (sum_of_evens, sum_of_odds).
    """
    return sum(n for n in numbers if n % 2 == 0), sum(n for n in numbers if n % 2 == 1)
# AI-generated docstring (Cursor AI):
AI_DOCSTRING = """
    Calculate the sum of even and odd numbers separately from a given list.
    
    Args:
        numbers (list[int]): A list of integers to process.
    
    Returns:
        tuple[int, int]: A tuple containing (sum of even numbers, sum of odd numbers).
    
    Examples:
        >>> sum_even_odd([1, 2, 3, 4, 5])
        (6, 9)
        >>> sum_even_odd([2, 4, 6])
        (12, 0)
"""
print("MANUAL DOCSTRING (Google Style):\n", sum_even_odd.__doc__)
print("\nAI-GENERATED DOCSTRING (Cursor AI):\n", AI_DOCSTRING)
print("="*50, "\nCOMPARISON:\nManual: Basic, concise, Google style\nAI: More detailed, includes examples, type hints [int]")

nums = list(map(int, input("Enter numbers (space-separated): ").split()))
evens, odds = sum_even_odd(nums)
print(f"Sum of evens: {evens}, Sum of odds: {odds}")

