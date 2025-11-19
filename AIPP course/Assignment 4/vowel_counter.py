#!/usr/bin/env python3
"""
vowel_counter.py

Counts vowels in a string. Usage:
  python vowel_counter.py            # interactive prompt
  python vowel_counter.py --include-y
  python vowel_counter.py --test     # run self-tests
"""

import argparse


def count_vowels(text, include_y: bool = False) -> int:
    """Count vowels in the given text.

    Args:
        text: Input value (will be converted to string). None becomes empty string.
        include_y: If True, treat 'y' and 'Y' as vowels.

    Returns:
        Integer count of vowel characters in the string.

    Examples:
        >>> count_vowels('Hello')
        2
        >>> count_vowels('rhythm')
        0
        >>> count_vowels('rhythm', include_y=True)
        1
    """
    if text is None:
        return 0
    vowels = set('aeiou')
    if include_y:
        vowels.add('y')
    s = str(text).lower()
    return sum(1 for ch in s if ch in vowels)


def breakdown(text, include_y: bool = False) -> dict:
    """Return a per-vowel breakdown (counts) for the text.

    Returns a dict mapping each vowel character to its count.
    """
    vowels = list('aeiou')
    if include_y:
        vowels.append('y')
    counts = {v: 0 for v in vowels}
    for ch in str(text).lower():
        if ch in counts:
            counts[ch] += 1
    return counts


def run_tests() -> None:
    # Basic tests (happy paths and a few edge cases)
    assert count_vowels('') == 0
    assert count_vowels(None) == 0
    assert count_vowels('bcd') == 0
    assert count_vowels('AEIOU') == 5
    assert count_vowels('Hello, World!') == 3  # e, o, o
    assert count_vowels('rhythm') == 0
    assert count_vowels('rhythm', include_y=True) == 1
    # breakdown check
    bd = breakdown('AaEeIiOoUuYy', include_y=True)
    assert bd['a'] == 2
    assert bd['e'] == 2
    assert bd['i'] == 2
    assert bd['o'] == 2
    assert bd['u'] == 2
    assert bd['y'] == 2
    print('All tests passed.')


def main() -> None:
    parser = argparse.ArgumentParser(description='Count vowels in a string.')
    parser.add_argument('--include-y', action='store_true', help="Consider 'y' a vowel")
    parser.add_argument('--test', action='store_true', help='Run self-tests')
    args = parser.parse_args()

    if args.test:
        run_tests()
        return

    try:
        text = input('Enter a string (or press Enter for empty): ')
    except EOFError:
        # When input is not available
        text = ''

    total = count_vowels(text, include_y=args.include_y)
    print(f'Total vowels: {total}')
    bd = breakdown(text, include_y=args.include_y)
    print('Breakdown:')
    for v, c in bd.items():
        print(f'  {v}: {c}')


if __name__ == '__main__':
    main()
