"""Calculator module with basic arithmetic operations."""

def add(a, b):
    """Add two numbers. Parameters: a (float), b (float). Returns: float - Sum of a and b."""
    return a + b

def subtract(a, b):
    """Subtract second number from first. Parameters: a (float), b (float). Returns: float - Difference of a and b."""
    return a - b

def multiply(a, b):
    """Multiply two numbers. Parameters: a (float), b (float). Returns: float - Product of a and b."""
    return a * b

def divide(a, b):
    """Divide first number by second. Parameters: a (float), b (float). Returns: float - Quotient. Raises: ZeroDivisionError - If b is zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# AI-generated docstrings (Cursor AI):
AI_MOD = "Calculator module with basic arithmetic operations.\nFunctions: add, subtract, multiply, divide.\nExamples: >>> add(5,3)\n8"
AI_FUNC = {'add': "Add nums.\nParams: a,b (float/int)\nReturns: float/int - Sum.\nEx: >>> add(2,3)\n5",
           'divide': "Divide a by b.\nParams: a,b (float/int)\nReturns: float - Quotient.\nRaises: ZeroDivisionError if b=0.\nEx: >>> divide(15,3)\n5.0"}

print("MANUAL (NumPy):\n", __doc__, "\n", add.__doc__, "\n" + "="*50)
print("AI:\n", AI_MOD, "\n", AI_FUNC['add'], "\n" + "="*50, "\nCOMPARISON:\nManual: Concise NumPy\nAI: Detailed with Examples\n" + "="*50)
a, b = float(input("Enter first number: ")), float(input("Enter second number: "))
print(f"Add: {add(a, b):.2f}, Sub: {subtract(a, b):.2f}, Mul: {multiply(a, b):.2f}", end="")
try:
    print(f", Div: {divide(a, b):.2f}")
except ZeroDivisionError as e:
    print(f", Error: {e}")

