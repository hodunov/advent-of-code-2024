def main():
    with open("input1-2.txt") as f:
        data_string = f.read()
    rows = [row.split() for row in data_string.strip().split("\n")]
    left, right = [], []
    for row in rows:
        left.append(int(row[0]))
        right.append(int(row[1]))
    return sum(right.count(item) * item for item in left)

if __name__ == "__main__":
    print(main())