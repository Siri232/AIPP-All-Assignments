def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True

# Test cases generated and justified by an AI helper
_tests = [
    (-5, False),
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (9, False),
    (25, False),
    (29, True),
    (97, True),
    (1000000, False),
    (1000003, True),
]
def _run_tests():
    failed = []
    for n, exp in _tests:
        res = is_prime(n)
        if res != exp:
            failed.append((n, exp, res))
    if not failed:
        print('All tests passed ({} cases).'.format(len(_tests)))
    else:
        print('Failed {} tests:'.format(len(failed)))
        for n, exp, res in failed:
            print(' n={} expected={} got={}'.format(n, exp, res))

if __name__ == '__main__':
    _run_tests()
    print('\nInteractive test: enter integers (empty line to quit).')
    try:
        while True:
            s = input('n = ').strip()
            if s == '':
                break
            try:
                x = int(s)
            except ValueError:
                print('Please enter a valid integer.')
                continue
            print('{} is {}prime.'.format(x, '' if is_prime(x) else 'not '))
    except (KeyboardInterrupt, EOFError):
        print('\nBye')
