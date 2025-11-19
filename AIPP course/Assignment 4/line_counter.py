#!/usr/bin/env python3
"""
line_counter.py

Provides a function to count lines in a text file, an interactive prompt, and a --test mode.

Usage:
  python line_counter.py               # interactive prompt
  python line_counter.py --path file.txt
  python line_counter.py --test        # run self-tests
"""

from __future__ import annotations
import argparse
import os
import tempfile
from typing import Optional


def count_lines(path: str) -> int:
    """Return the number of lines in the file at `path`.

    Args:
        path: Path to the file to read. Should point to a text file (commonly .txt), but any file path is accepted.

    Returns:
        The number of lines in the file as an int.

    Raises:
        FileNotFoundError: If the file does not exist.
        IsADirectoryError: If the path points to a directory.
        OSError: For other I/O errors.

    Implementation notes:
    - Opens the file with UTF-8 encoding and `errors='replace'` to avoid UnicodeDecodeError on mixed encodings.
    - Uses an iterator to count lines efficiently without loading the whole file.
    """
    if path is None:
        raise ValueError('path cannot be None')
    path = str(path)
    if not os.path.exists(path):
        raise FileNotFoundError(f'No such file: {path}')
    if os.path.isdir(path):
        raise IsADirectoryError(f'Path is a directory: {path}')

    count = 0
    # Use a buffered iterator to count lines efficiently.
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        for _ in f:
            count += 1
    return count


def prompt_and_count() -> None:
    """Interactive loop: prompt the user for a file path and print counts.

    The loop continues until the user inputs an empty line or one of the
    exit commands: 'q', 'quit', 'exit'. This is handy for manually checking
    multiple files without restarting the script.
    """
    print("Interactive line counter. Enter a file path to count lines.")
    print("Enter an empty line or 'q'/'quit'/'exit' to finish.")
    while True:
        try:
            path = input('Path> ').strip()
        except EOFError:
            print('\nNo more input. Exiting.')
            break

        if not path or path.lower() in {'q', 'quit', 'exit'}:
            print('Exiting interactive mode.')
            break

        try:
            total = count_lines(path)
        except Exception as exc:
            print(f'Error: {exc}')
            continue

        print(f'Total lines: {total}')

    # interactive returns nothing
    return


def run_tests() -> None:
    """Run a few quick self-tests using temporary files."""
    # Test 1: empty file
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.txt') as t1:
        t1_path = t1.name
    try:
        assert count_lines(t1_path) == 0
    finally:
        os.remove(t1_path)

    # Test 2: file with 3 lines (last line with newline)
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.txt') as t2:
        t2.write('line1\nline2\nline3\n')
        t2_path = t2.name
    try:
        assert count_lines(t2_path) == 3
    finally:
        os.remove(t2_path)

    # Test 3: file without trailing newline on last line
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.txt') as t3:
        t3.write('one\ntwo\nthree')
        t3_path = t3.name
    try:
        assert count_lines(t3_path) == 3
    finally:
        os.remove(t3_path)

    # Test 4: non-utf8 bytes - ensure no crash (we write utf-8 bytes here but test that 'errors=replace' works)
    with tempfile.NamedTemporaryFile('wb', delete=False, suffix='.txt') as t4:
        t4.write(b'alpha\n\xc3\x28\nbeta\n')  # contains an invalid sequence 0xc3 0x28
        t4_path = t4.name
    try:
        # Should count 3 lines even if there's an invalid byte sequence
        assert count_lines(t4_path) == 3
    finally:
        os.remove(t4_path)

    # Test 5: passing directory raises
    tmpdir = tempfile.mkdtemp()
    try:
        raised = False
        try:
            count_lines(tmpdir)
        except IsADirectoryError:
            raised = True
        assert raised
    finally:
        try:
            os.rmdir(tmpdir)
        except OSError:
            pass

    print('All tests passed.')


def main() -> None:
    parser = argparse.ArgumentParser(description='Count lines in a text file.')
    parser.add_argument('--path', type=str, help='Path to the file to count lines')
    parser.add_argument('--test', action='store_true', help='Run self-tests')
    parser.add_argument('--interactive', action='store_true', help='Prompt for a file path interactively')
    args = parser.parse_args()

    if args.test:
        run_tests()
        return

    if args.path:
        try:
            total = count_lines(args.path)
            print(f'Total lines: {total}')
        except Exception as exc:
            print(f'Error: {exc}')
        return

    # Default: interactive prompt
    prompt_and_count()


if __name__ == '__main__':
    main()
