def is_valid_email(s):
    s = s.strip()
    if not s or ' ' in s or s.count('@') != 1 or '..' in s: return False
    if not (s[0].isalnum() and s[-1].isalnum()): return False
    local, domain = s.split('@')
    if '.' not in domain or not domain[0].isalnum(): return False
    return True

tests = [
    ("user@example.com", True),
    ("user.name@sub.example.co", True),
    ("user@com", False),
    ("@example.com", False),
    ("user@", False),
    ("user@@example.com", False),
    ("user@.com", False),
    ("user@example.com.", False),
    (" user@example.com", True),
    ("user+tag@example.com", True),
    ("user-name@example.com", True),
    ("", False),
    ("a@b.c", True),
    (".user@example.com", False),
    ("user@example", False),
    ("user@exa mple.com", False),
    ("user..name@example.com", False),
    ("user@example..com", False),
]

for e, exp in tests:
    r = is_valid_email(e)
    if r != exp:
        print("FAIL:", e, "got", r, "expected", exp)
        break
else:
    print("All tests passed")

# Interactive check
email = input("Enter an email to validate: ")
print("Valid" if is_valid_email(email) else "Invalid")