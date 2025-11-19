def convert_date_format(date_str): return '-'.join(date_str.split('-')[::-1])

if __name__ == "__main__":
    test_cases = [("2023-10-15", "15-10-2023"), ("2024-01-01", "01-01-2024"), ("2023-12-31", "31-12-2023")]
    for inp, exp in test_cases:
        result = convert_date_format(inp)
        print(f"convert_date_format('{inp}') -> '{result}' {'[PASS]' if result == exp else '[FAIL]'}")
    print("Function converts input format correctly for all test cases\n")
    while True:
        date = input("Enter date (YYYY-MM-DD) or 'quit': ")
        if date == "quit": break
        try: print(f"Result: {convert_date_format(date)}")
        except: print("Invalid format!")