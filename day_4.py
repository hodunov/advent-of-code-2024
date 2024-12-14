DIRECTIONS: list[tuple[int, int]] = [
    (-1, 0),
    (-1, -1),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

TARGET_WORD: str = "XMAS"


def is_within_bounds(grid: list[str], x: int, y: int) -> bool:
    return (0 <= y < len(grid)) and (0 <= x < len(grid[0].strip()))


def check_direction(
    grid: list[str],
    start_x: int,
    start_y: int,
    direction: tuple[int, int],
) -> bool:
    dy, dx = direction

    end_x = start_x + dx * 3
    end_y = start_y + dy * 3

    if not is_within_bounds(grid, end_x, end_y):
        return False

    for i, target_char in enumerate(TARGET_WORD):
        current_x = start_x + dx * i
        current_y = start_y + dy * i
        if grid[current_y][current_x] != target_char:
            return False

    return True


def main():
    with open("day4.txt") as f:
        grid = f.readlines()
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0].strip("\n"))):
            if grid[y][x] == "X":
                for direction in DIRECTIONS:
                    if check_direction(grid, x, y, direction):
                        count += 1
    return count


if __name__ == "__main__":
    print(main())
