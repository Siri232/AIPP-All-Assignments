def normalize_gender(raw: str) -> str:
    """Map many user inputs to canonical keys: male, female, neutral, none."""
    g = (raw or "").strip().lower()

    male_terms = {"m", "male", "man", "boy"}
    female_terms = {"f", "female", "woman", "girl"}
    neutral_terms = {
        "nb", "enby", "nonbinary", "non-binary",
        "gender-neutral", "gender neutral", "neutral", "x", "mx"
    }
    none_terms = {
        "", "na", "n/a", "none", "prefer not to say",
        "unspecified", "unknown", "skip"
    }

    if g in male_terms:
        return "male"
    if g in female_terms:
        return "female"
    if g in neutral_terms:
        return "neutral"
    if g in none_terms:
        return "none"
    # Fallback to neutral if it's something else
    return "neutral"


def greet_user(name: str, gender: str) -> str:
    """Return an inclusive greeting with an appropriate title."""
    titles = {
        "male": "Mr.",
        "female": "Ms.",
        "neutral": "Mx.",
        "none": ""  # No title used
    }
    key = normalize_gender(gender)
    title = titles.get(key, "Mx.")
    space = " " if title else ""
    return f"Hello, {title}{space}{name}! Welcome."


if __name__ == "__main__":
    name_input = input("Enter your name: ").strip() or "Friend"
    gender_input = input(
        "Enter your gender (male/female/non-binary/neutral/none or press Enter to skip): "
    )
    print(greet_user(name_input, gender_input))