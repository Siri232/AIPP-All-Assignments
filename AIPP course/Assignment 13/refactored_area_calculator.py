import math

calc_area = lambda shape, x, y=0: {"rectangle": x*y, "square": x*x, "circle": math.pi*x*x}.get(shape)

while True:
    s = input("Shape (rectangle/square/circle/exit): ").lower()
    if s == "exit": break
    try:
        x = float(input("Value 1: "))
        y = float(input("Value 2 (0 for circle/square): ") or 0)
        print(f"Area: {calc_area(s, x, y):.2f}\n")
    except: print("Invalid input\n")
