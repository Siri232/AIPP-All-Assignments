"""Leap year checker with a small CLI.

This module provides a single function :func:`is_leap_year` which implements
the Gregorian leap-year rules and a tiny command-line prompt so a user can
type years to check interactively.

Rules implemented:
- Years divisible by 4 are leap years,
- except years divisible by 100 are not leap years,
- except years divisible by 400 are leap years.

Example:
  >>> is_leap_year(2000)
  True
  >>> is_leap_year(1900)
  False

The script also supports running as a script and will prompt for input.
"""

from typing import Any


def is_leap_year(year: int) -> bool:
  """Return True if ``year`` is a leap year (Gregorian rules).

  Args:
    year: integer year to check. A TypeError is raised if a non-int is
      supplied. Negative and zero years are handled arithmetically.

  Returns:
    True if ``year`` is a leap year, otherwise False.
  """

  if not isinstance(year, int):
    raise TypeError("year must be an integer")

  return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)


def _prompt_loop() -> None:
  """Simple input loop for checking years from the user."""

  prompt = "Enter a year (or blank to exit): "
  while True:
    try:
      s = input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
      print()  # newline
      break

    if s == "":
      break

    try:
      year = int(s)
    except ValueError:
      print("Please enter a valid integer year.")
      continue

    try:
      if is_leap_year(year):
        print(f"{year} is a leap year.")
      else:
        print(f"{year} is not a leap year.")
    except Exception as exc:  # defensive: should not normally happen
      print(f"Error checking year: {exc}")


if __name__ == "__main__":
  _prompt_loop()
