numbers = [1, 2, 3]

index = int(input("Enter index to access (0-2): "))

if 0 <= index < len(numbers):
    print(f"Value at index {index}: {numbers[index]}")
else:
    print(f"Error: Index {index} is out of range. List has {len(numbers)} elements.")
