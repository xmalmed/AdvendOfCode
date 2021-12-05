from utils.puzzle import Puzzle
from parse import parse
from collections import defaultdict
from numpy import sign


def is_vertical(x1, y1, x2, y2):
    return x1 == x2


def is_horizontal(x1, y1, x2, y2):
    return y1 == y2


def is_diagonal(x1, y1, x2, y2):
    return abs(x1 - x2) == abs(y1 - y2)


def update_field(x, y):
    field[(x, y)] += 1


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    field = defaultdict(lambda: 0)
    for d in data:
        x1, y1, x2, y2 = parse("{:d},{:d} -> {:d},{:d}", d)
        if is_vertical(x1, y1, x2, y2):
            for i in range(min(y1, y2), max(y1, y2) + 1):
                update_field(x1, i)
        elif is_horizontal(x1, y1, x2, y2):
            for i in range(min(x1, x2), max(x1, x2) + 1):
                update_field(i, y1)
        elif is_diagonal(x1, y1, x2, y2):
            dx = sign(x1 - x2)
            dy = sign(y1 - y2)
            s = abs(x1 - x2)
            for i in range(s + 1):
                update_field(x2 + dx * i, y2 + dy * i)
        else:
            pass

    danger = len([s for s in field.values() if s >= 2])
    # print("Number of high dangers: ", danger)
    print("Number of high even diagonal dangers: ", danger)
