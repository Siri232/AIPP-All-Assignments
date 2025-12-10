def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("--- Python Factorial Calls ---")
user_input = input("Enter a non-negative integer to calculate its factorial: ")
try:
    num_to_factorialize = int(user_input)
    if num_to_factorialize < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {num_to_factorialize} = {factorial(num_to_factorialize)}")
except ValueError:
    print("Invalid input. Please enter an integer.")
