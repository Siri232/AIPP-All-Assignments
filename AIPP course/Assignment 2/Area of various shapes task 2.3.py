def explain_and_run_area_calculator():
    print("Welcome! This program calculates the area of multiple shapes.")
    print("Let's go through the code step by step, just like Gemini explaining it.\n")
    
    # Step 1: Ask the user to choose a shape
    print("Line 1: Asking the user to select a shape.")
    print("Available shapes: circle, rectangle, triangle, square, trapezoid, ellipse")
    shape = input("Enter shape name: ").lower()
    
    # Step 2: Use if-elif statements to handle different shapes
    print("\nLine 2: Using if-elif statements to handle each shape type.")
    
    if shape == "circle":
        print("Line 3: Asking for radius to calculate area of a circle.")
        radius = float(input("Enter radius: "))
        area = 3.14159 * radius ** 2
        print(f"Line 4: Area of circle = π * r² = {area:.2f}")
        
    elif shape == "rectangle":
        print("Line 3: Asking for length and width to calculate area of a rectangle.")
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print(f"Line 4: Area of rectangle = length * width = {area:.2f}")
        
    elif shape == "triangle":
        print("Line 3: Asking for base and height to calculate area of a triangle.")
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print(f"Line 4: Area of triangle = ½ * base * height = {area:.2f}")
        
    elif shape == "square":
        print("Line 3: Asking for side to calculate area of a square.")
        side = float(input("Enter side length: "))
        area = side ** 2
        print(f"Line 4: Area of square = side² = {area:.2f}")
        
    elif shape == "trapezoid":
        print("Line 3: Asking for bases and height to calculate area of a trapezoid.")
        base1 = float(input("Enter base 1: "))
        base2 = float(input("Enter base 2: "))
        height = float(input("Enter height: "))
        area = 0.5 * (base1 + base2) * height
        print(f"Line 4: Area of trapezoid = ½ * (base1 + base2) * height = {area:.2f}")
        
    elif shape == "ellipse":
        print("Line 3: Asking for semi-major and semi-minor axes to calculate area of an ellipse.")
        a = float(input("Enter semi-major axis (a): "))
        b = float(input("Enter semi-minor axis (b): "))
        area = 3.14159 * a * b
        print(f"Line 4: Area of ellipse = π * a * b = {area:.2f}")
        
    else:
        print("Line 5: Invalid shape entered. Exiting program.")
        return
    
    print("\nGemini-style explanation complete. Your calculated area is shown above!")

# Run the function
explain_and_run_area_calculator()
