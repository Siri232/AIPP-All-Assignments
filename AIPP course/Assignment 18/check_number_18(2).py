def check_number(num):
    if num > 0:
        print("The number is positive")
    elif num < 0:
        print("The number is negative")
    else:
        print("The number is zero")

print("--- Python Function Calls ---")
user_input = input("Enter a number to check: ")
try:
    num_to_check = int(user_input)
    check_number(num_to_check)
except ValueError:
    print("Invalid input. Please enter an integer.")
