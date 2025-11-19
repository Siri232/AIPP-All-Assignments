def count_down(n):
    while n >= 0:
        print(n)
        n -= 1

n = int(input("Enter a number to count down from: "))
count_down(n)
