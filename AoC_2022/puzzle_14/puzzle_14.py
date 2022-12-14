from utils.puzzle import Puzzle


def move_sand(x, y, r):
    if y + 1 >= ABYSS + 5:
        return False
    for dx, dy in [(0, 1), (-1, 1), (1, 1), (0, 0)]:
        if dy == 0:
            r[(x, y)] = 1
            return True
        if (x + dx, y + dy) not in r:
            return move_sand(x + dx, y + dy, r)
        else:
            continue
    return 'wtf'


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    rocks = {}
    for line in data:
        parts = line.split(' -> ')
        first = True
        for p in parts:
            x, y = p.split(',')
            if first:
                first = False
                px = int(x)
                py = int(y)
            else:
                x = int(x)
                y = int(y)
                if x == px:
                    for ty in range(min(y, py), max(y, py) + 1):
                        rocks[(x, ty)] = 0
                if y == py:
                    for tx in range(min(x, px), max(x, px) + 1):
                        rocks[(tx, y)] = 0
                px = x
                py = y

    ABYSS = max(rocks.keys(), key=lambda x: x[1])[1] + 2

    while True:
        more_sand = move_sand(500, 0, rocks)
        if not more_sand:
            break

    print(f'part 1: sand units: {sum(rocks.values())}')

    for x in range(495 - ABYSS, 505 + ABYSS):
        rocks[x, ABYSS] = 0

    while (500, 0) not in rocks:
        more_sand = move_sand(500, 0, rocks)
        if not more_sand:
            break

    print(f'part 2: sand units: {sum(rocks.values())}')
