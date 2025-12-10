class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print("Car Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Read input from stdin (CodeChef-friendly)
brand = input().strip()
model = input().strip()
year = input().strip()

# Create object
car = Car(brand, model, year)

# Display details
car.display_details()
