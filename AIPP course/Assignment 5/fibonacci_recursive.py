"""
Fibonacci Number Calculator using Recursion
This module contains a function to calculate the nth Fibonacci number
using a recursive approach. The Fibonacci sequence is a series of numbers
where each number is the sum of the two preceding ones, starting from 0 and 1.
Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
Author: Generated for AIPP course
"""
def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    This function uses the mathematical definition of Fibonacci numbers:
    - F(0) = 0
    - F(1) = 1
    - F(n) = F(n-1) + F(n-2) for n > 1
    
    Args:
        n (int): The position in the Fibonacci sequence (non-negative integer).
                 n=0 returns 0, n=1 returns 1, n=2 returns 1, etc.
    
    Returns:
        int: The nth Fibonacci number.
    
    Raises:
        ValueError: If n is negative.
        RecursionError: If n is too large (Python's recursion limit).
    
    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(5)
        5
        >>> fibonacci(10)
        55
    
    Note:
        This recursive implementation has exponential time complexity O(2^n),
        making it inefficient for large values of n. For production use,
        consider iterative or memoized versions.
    """
    # Base case 1: If n is 0, return 0 (first Fibonacci number)
    if n == 0:
        return 0
    # Base case 2: If n is 1, return 1 (second Fibonacci number)
    if n == 1:
        return 1
    # Input validation: Check if n is negative
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    # Recursive case: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
    # This breaks down the problem into smaller subproblems
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    """
    Main function to get user input and calculate Fibonacci number.
    """
    # Get user input for the Fibonacci position
    try:
        n = int(input("Enter the position (n) to calculate Fibonacci number: "))
        result = fibonacci(n)
        print(f"Fibonacci({n}) = {result}")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid non-negative integer.")
    except RecursionError:
        print("Error: Number too large. Please enter a smaller value (n < 35 recommended).")
# Entry point: Run the main function if this script is executed directly
if __name__ == "__main__":
    main()

