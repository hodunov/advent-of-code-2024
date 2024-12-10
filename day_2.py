def is_safe(array):
    if len(array) <= 1:
        return 1

    diffs = [array[i + 1] - array[i] for i in range(len(array) - 1)]
    is_asc = all(0 < x < 4 for x in diffs)
    is_desc = all(-4 < x < 0 for x in diffs)
    return 1 if is_asc or is_desc else 0


def main():
    with open("input2.txt") as f:
        data_string = f.read()
    rows = [list(map(int, row.split())) for row in data_string.strip().split("\n")]
    safe_count = 0
    for row in rows:
        safe_count += is_safe(row)

    return safe_count


if __name__ == "__main__":
    print(main())
