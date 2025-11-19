"""Centimeters to inches converter with a small CLI.

Provides :func:`cm_to_inches` and a prompt loop for quick manual testing.

Conversion: 1 inch = 2.54 cm
"""

def cm_to_inches(cm: float) -> float:
    """Convert centimeters to inches.

    Args:
        cm: length in centimeters (int or float).

    Returns:
        Equivalent length in inches as a float.

    Raises:
        TypeError: if ``cm`` is not a number.
    """

    if not isinstance(cm, (int, float)):
        raise TypeError("cm must be a number (int or float)")

    return float(cm) / 2.54


def _prompt_loop() -> None:
    """A tiny CLI loop to accept user input and print conversion results."""

    prompt = "Enter length in centimeters (or blank to exit): "
    while True:
        try:
            s = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if s == "":
            break

        try:
            val = float(s)
        except ValueError:
            print("Please enter a valid number (e.g. 12.7).")
            continue

        inches = cm_to_inches(val)
        print(f"{val} cm = {inches:.4f} in")


if __name__ == "__main__":
    _prompt_loop()
