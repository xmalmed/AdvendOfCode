from utils.puzzle import Puzzle
from numpy import array

ADJACENT = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def is_minimum(cave, y, x):
    return all([cave[y + a[0], x + a[1]] > cave[y, x] for a in ADJACENT])


def map_basin(cave, y, x):
    basin_size = 0
    for a in ADJACENT:
        if 0 <= cave[y + a[0], x + a[1]] < 9:
            cave[y + a[0], x + a[1]] = -1
            basin_size += 1
            basin_size += map_basin(cave, y + a[0], x + a[1])
    return basin_size


if __name__ == '__main__':
    p = Puzzle()
    data = p.load_input(string=True)
    # data = p.load_input('input_test.txt', string=True)

    # part 1
    x_size = len(data[0])
    y_size = len(data)
    cave = [[11] * (x_size + 2)]
    for line in data:
        cave.append([11, ] + [int(ch) for ch in line] + [11, ])
    cave.append([11] * (x_size + 2))
    cave = array(cave)

    basins = []
    total_risk = 0
    for y in range(1, y_size + 1):
        for x in range(1, x_size + 1):
            if is_minimum(cave, y, x) and cave[y, x] >= 0:
                total_risk += cave[y, x] + 1
                cave[y, x] = -1
                total_basin_size = map_basin(cave, y, x) + 1
                basins.append(total_basin_size)

    basins.sort()
    print("Total risk is: ", total_risk)
    print("Three largest basins: ", basins[-3:])
    print(basins[-3] * basins[-2] * basins[-1])
