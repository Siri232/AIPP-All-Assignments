# GitHub Copilot Generated Code
# Program to calculate the sum of odd and even numbers in a list

def sum_odd_even(numbers):
    """Return the sum of odd and even numbers from the given list."""
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    even_sum = sum(num for num in numbers if num % 2 == 0)
    return odd_sum, even_sum

if __name__ == "__main__":
    try:
        # Take user input as space-separated numbers
        nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
        odd_sum, even_sum = sum_odd_even(nums)
        print("Numbers:", nums)
        print("Sum of odd numbers:", odd_sum)
        print("Sum of even numbers:", even_sum)
    except ValueError:
        print("Invalid input! Please enter integer values only.")
