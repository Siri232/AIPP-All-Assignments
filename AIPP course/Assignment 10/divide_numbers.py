def divide_numbers(a, b):
    """
    Divide two numbers with proper error handling.
    Handles ZeroDivisionError and TypeError exceptions. 
    Args:
        a (float): The dividend
        b (float): The divisor
    
    Returns:
        float: The result of a / b
    
    Raises:
        ZeroDivisionError: If b is zero
        TypeError: If arguments are not numbers
    """
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Cannot divide by zero!")
    except TypeError:
        raise TypeError("Error: Both arguments must be numbers!")
if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = divide_numbers(a, b)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numbers!")
    except (ZeroDivisionError, TypeError) as e:
        print(e)