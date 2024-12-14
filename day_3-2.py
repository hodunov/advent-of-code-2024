import re
from typing import Iterator, Match

FILE_NAME = "input3-2.txt"
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
        data = "".join(part.split("don't()")[0] for part in data_string.split("do()"))
        matches = re.finditer(PATTERN, data)
        return calculate_total(matches)
    except FileNotFoundError:
        print(f"File {FILE_NAME} not found")
        return 0
    except Exception as e:
        print(f"There was an unexpected error: {e}")
        return 0


if __name__ == "__main__":
    print(main())
