def main():
    with open("input1.txt") as f:
        data_string = f.read()
    rows = [row.split() for row in data_string.strip().split("\n")]
    left, right = [], []
    for row in rows:
        left.append(int(row[0]))
        right.append(int(row[1]))
    left.sort()
    right.sort()
    return sum(abs(x - y) for x, y in zip(left, right))


if __name__ == "__main__":
    print(main())
    