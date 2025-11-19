import numpy as np

def f(x): return 2*x**3 + 4*x + 5
def df(x): return 6*x**2 + 4

x = float(input("Enter initial x: "))
lr = float(input("Enter learning rate (0.0001-0.001): "))
itr = int(input("Enter iterations: "))

for _ in range(itr):
    x -= lr * df(x)

print(f"Minimum at x: {x:.4f}")
print(f"Minimum value: {f(x):.4f}")
