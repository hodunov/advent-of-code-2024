import re
from typing import Iterator, Match

FILE_NAME = "input3.txt"
PATTERN = r"mul\((?P<first>\d+),(?P<second>\d+)\)"


def extract_numbers(match: Match) -> tuple[int, int]:
    first = int(match.group("first"))
    second = int(match.group("second"))
    return first, second


def calculate_total(matches: Iterator[Match]) -> int:
    return sum(
        first * second
        for match in matches
        for first, second in [extract_numbers(match)]
    )


def main() -> int:
    try:
        with open(FILE_NAME) as f:
            data_string = f.read()
        matches = re.finditer(PATTERN, data_string)
        return calculate_total(matches)
    except FileNotFoundError:
        print(f"File {FILE_NAME} not found")
        return 0
    except Exception as e:
        print(f"There was an unexpected error: {e}")
        return 0


if __name__ == "__main__":
    print(main())
