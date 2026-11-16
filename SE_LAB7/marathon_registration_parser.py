def format_bib_name(name):
    """Uppercase a runner name and limit it to 12 characters."""
    if not isinstance(name, str):
        return ""
    return name.strip().upper()[:12]


def parse_finish_time(text):
    """Convert H:MM:SS to seconds; return None for invalid input."""
    if not isinstance(text, str):
        return None

    parts = text.split(":")
    if len(parts) != 3 or any(not part.isascii() or not part.isdigit() for part in parts):
        return None

    try:
        hours, minutes, seconds = map(int, parts)
    except (ValueError, OverflowError):
        return None

    if minutes > 59 or seconds > 59:
        return None

    return hours * 3600 + minutes * 60 + seconds


def average_split(text):
    """Average whole-number split times; return None for invalid input."""
    if not isinstance(text, str):
        return None

    parts = text.split()
    if not parts or any(not part.isascii() or not part.isdigit() for part in parts):
        return None

    try:
        splits = [int(part) for part in parts]
        return sum(splits) / len(splits)
    except (ValueError, OverflowError):
        return None


def main():
    print("==== Running format_bib_name ====")
    value = input("Enter the name to print on the bib: ")
    print("Bib name:", format_bib_name(value))

    print("\n==== Running parse_finish_time ====")
    value = input("Enter a finish time as H:MM:SS (e.g. 3:45:10): ")
    print("Finish time in seconds:", parse_finish_time(value))

    print("\n==== Running average_split ====")
    value = input("Enter your 5 km split times in minutes separated by spaces (e.g. 25 26 24): ")
    print("Average split (minutes):", average_split(value))


if __name__ == "__main__":
    main()

