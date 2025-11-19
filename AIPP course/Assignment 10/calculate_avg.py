def calculate_average(scores):
    return sum(scores) / len(scores)

def find_highest(scores):
    return max(scores)

def find_lowest(scores):
    return min(scores)

def process_scores(scores):
    print(f"Average: {calculate_average(scores)}")
    print(f"Highest: {find_highest(scores)}")
    print(f"Lowest: {find_lowest(scores)}")

if __name__ == "__main__":
    user_scores = list(map(float, input("Enter scores separated by spaces: ").split()))
    process_scores(user_scores)