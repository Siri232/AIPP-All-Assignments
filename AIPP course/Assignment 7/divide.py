# Debug the following code
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
print(divide(a, b))
