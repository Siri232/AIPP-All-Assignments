def find_common():
    list_a = input("Enter items for list A separated by spaces: ").split()
    list_b = input("Enter items for list B separated by spaces: ").split()
    common = list(set(list_a) & set(list_b))
    print("Common items:", common)

find_common()