def sum_to_n(n):
    """Calculate the sum of the first n natural numbers using while loop."""
    if n < 0:
        return None
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

if __name__ == "__main__":
    try:
        n = int(input("Enter a positive integer n to calculate sum of first n numbers: "))
        result = sum_to_n(n)
        if result is not None:
            print(f"The sum of the first {n} numbers is: {result}")
            if n <= 10:
                print(f"Calculation: {' + '.join(str(i) for i in range(1, n + 1))} = {result}")
        else:
            print("Error: Please enter a non-negative integer.")
    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print(f"An error occurred: {e}")

