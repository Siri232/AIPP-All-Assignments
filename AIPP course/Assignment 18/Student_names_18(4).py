# Function to print student names
def print_students(students):
    print("Student List:")
    for name in students:
        print(name)

# User input
user_input = input("Enter student names separated by commas: ")

# Convert input string to list
students = [name.strip() for name in user_input.split(",")]

# Test the function
print_students(students)
