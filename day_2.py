def main():
    with open("input2.txt") as f:
        data_string = f.read()
    rows = [list(map(int, row.split())) for row in data_string.strip().split("\n")]
    safe_count = 0

    for row in rows:
        diff = {row[i + 1] - row[i] for i in range(len(row) - 1)}
        if all(0 < x < 4 for x in diff) or all(-4 < x < 0 for x in diff):
            safe_count += 1

    return safe_count


if __name__ == "__main__":
    print(main())
