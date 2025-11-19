def assign_grade(score):
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        return "Invalid"
    grades = [(90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F")]
    for threshold, grade in grades:
        if score >= threshold:
            return grade

# Generate test cases using loops
test_cases = []
# Boundary values using loops
for boundary in [90, 100, 89, 80, 79, 70, 69, 60, 59, 0]:
    test_cases.append(boundary)
# Invalid inputs
for invalid in [-5, 105, "eighty", None]:
    test_cases.append(invalid)

print("Test Cases:")
for tc in test_cases:
    print(f"assign_grade({tc!r}) = {assign_grade(tc)}")

# User input with loop
if __name__ == "__main__":
    while True:
        try:
            score = input("\nEnter score to test (or 'q' to quit): ")
            if score.lower() == 'q':
                break
            print(f"Grade: {assign_grade(float(score))}")
        except ValueError:
            print("Grade: Invalid")

