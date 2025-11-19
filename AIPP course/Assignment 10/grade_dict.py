def grade(score):
    """Determine letter grade using dictionary mapping - shortest version."""
    return next((g for threshold, g in [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D')] if score >= threshold), 'F')


if __name__ == "__main__":
    try:
        score = float(input("Enter score (0-100): "))
        print(f"Grade: {grade(score)}" if 0 <= score <= 100 else "Error: Score must be between 0 and 100!")
    except ValueError:
        print("Error: Please enter a valid number!")

