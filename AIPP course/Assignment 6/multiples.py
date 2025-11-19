def print_multiples(number):
    """Print the first 10 multiples of a given number."""
    for i in range(1, 11):
        print(f"{number} × {i} = {number * i}")


if __name__ == "__main__":
    print_multiples(int(input("Enter a number: ")))

