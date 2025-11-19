def classify_age(age):
    """Classify age into different groups using nested if-elif-else."""
    if age < 0:
        print("Invalid age! Age cannot be negative.")
    elif age <= 2:
        print(f"Age {age}: Infant/Toddler")
    elif age <= 12:
        print(f"Age {age}: Child")
    elif age <= 19:
        print(f"Age {age}: Teenager")
    elif age <= 39:
        if age <= 29:
            print(f"Age {age}: Young Adult (20-29)")
        else:
            print(f"Age {age}: Adult (30-39)")
    elif age <= 64:
        if age <= 49:
            print(f"Age {age}: Middle-aged (40-49)")
        else:
            print(f"Age {age}: Middle-aged (50-64)")
    else:
        if age <= 79:
            print(f"Age {age}: Senior (65-79)")
        else:
            print(f"Age {age}: Elderly (80+)")

if __name__ == "__main__":
    classify_age(int(input("Enter age: ")))

