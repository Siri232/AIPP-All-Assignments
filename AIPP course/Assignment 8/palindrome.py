import re
def is_sentence_palindrome(sentence):
    s = re.sub(r'[^a-z]', '', sentence.lower())
    return s == s[::-1]

# Test cases
tests = [
    ("A man a plan a canal Panama", True),
    ("race a car", False),
    ("", True),
    ("a", True),
    ("Madam, I'm Adam", True),
    ("Was it a car or a cat I saw?", True),
    ("hello", False),
    ("A Santa at NASA", True),
    ("No 'x' in Nixon", True),
    ("Able was I ere I saw Elba", True),
]

for test, expected in tests:
    result = is_sentence_palindrome(test)
    print(f"'{test}' -> {result} (expected {expected}) {'PASS' if result == expected else 'FAIL'}")

print("\n" + "="*50)
print("Enter your own sentences to test (or 'quit' to exit):")
while True:
    sentence = input("\nEnter a sentence: ").strip()
    if sentence.lower() in ['quit', 'exit', 'q']:
        break
    result = is_sentence_palindrome(sentence)
    print(f"Result: {result}")

