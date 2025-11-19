# Generated Code
# Program to find the sum of squares of numbers entered by the user

def sum_of_squares(numbers):
    """Return the sum of squares of given numbers."""
    return sum(num ** 2 for num in numbers)

if __name__ == "__main__":
    try:
        # Take user input as space-separated numbers
        nums = list(map(float, input("Enter numbers separated by spaces: ").split()))
        print("Numbers:", nums)
        print("Sum of squares:", sum_of_squares(nums))
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
