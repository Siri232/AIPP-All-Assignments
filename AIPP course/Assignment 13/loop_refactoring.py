s = input("Enter numbers separated by spaces (press Enter for 1..10): ").strip()
nums = map(int, s.split()) if s else range(1, 11)
print([n*n for n in nums])