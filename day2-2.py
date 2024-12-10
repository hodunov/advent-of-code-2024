def is_safe(array):
    if len(array) <= 1:
        return 1

    diffs = [array[i + 1] - array[i] for i in range(len(array) - 1)]
    is_asc = all(0 < x < 4 for x in diffs)
    is_desc = all(-4 < x < 0 for x in diffs)
    return 1 if is_asc or is_desc else 0


def problem_dampener(original_list):
    safety_level = is_safe(original_list)
    if safety_level == 0:
        for i in range(len(original_list)):
            arr_copy = original_list.copy()
            arr_copy.pop(i)
            if is_safe(arr_copy):
                return 1
        return 0
    return safety_level


def main():
    with open("input2-2.txt") as f:
        data_string = f.read()
    rows = [list(map(int, row.split())) for row in data_string.strip().split("\n")]
    safe_count = 0
    for row in rows:
        safe_count += problem_dampener(row)
    return safe_count


if __name__ == "__main__":
    print(main())
