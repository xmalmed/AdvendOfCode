from utils.puzzle import Puzzle
import re
import numpy as np

R = np.array([[0, 1], [-1, 0]])


def move_one(p, dir):
    n = tuple(p + dir)
    if n in m:
        if m[n] == ".":
            return p + dir
        elif m[n] == "#":
            return None
    else:
        if part_one:
            n = p - dir
            while tuple(n) in m:
                n = n - dir
            n = tuple(n + dir)
            if m[n] == ".":
                return np.array(n)
            elif m[n] == "#":
                return None
        else:
            n, nd = move_over_dice(p, dir)
            if m[n] == ".":
                global d
                d = nd
                return np.array(n)
            else:
                return None


def move_over_dice(p, d):
    # 1
    if p[0] >= 100 and p[1] == 49 and tuple(d) == (0, 1):
        n = (99, 50 + p[0] - 100)
        nd = rotate(d, "R")
    elif p[0] == 99 and 50 <= p[1] <= 99 and tuple(d) == (1, 0):
        n = (100 + p[1] - 50, 49)
        nd = rotate(d, "L")
    # 2
    elif p[0] <= 49 and p[1] == 100 and tuple(d) == (0, -1):
        n = (50, 50 + p[0])
        nd = rotate(d, "R")
    elif p[0] == 50 and 50 <= p[1] <= 99 and tuple(d) == (-1, 0):
        n = (p[1] - 50, 100)
        nd = rotate(d, "L")
    # 3
    elif p[0] == 49 and p[1] >= 150 and tuple(d) == (1, 0):
        n = (50 + p[1] - 150, 149)
        nd = rotate(d, "L")
    elif p[0] >= 50 and p[1] == 149 and tuple(d) == (0, 1):
        n = (49, p[0] - 50 + 150)
        nd = rotate(d, "R")
    # 4
    elif p[0] == 149 and p[1] <= 49 and tuple(d) == (1, 0):
        n = (99, 149 - p[1])
        nd = -1 * d
    elif p[0] == 99 and p[1] >= 100 and tuple(d) == (1, 0):
        n = (149, 149 - p[1])
        nd = -1 * d
    # 5
    elif p[0] == 50 and p[1] <= 49 and tuple(d) == (-1, 0):
        n = (0, 149 - p[1])
        nd = -1 * d
    elif p[0] == 0 and p[1] <= 149 and tuple(d) == (-1, 0):
        n = (50, 149 - p[1])
        nd = -1 * d
    # 6
    elif p[0] <= 99 and p[1] == 0 and tuple(d) == (0, -1):
        n = (0, p[0] - 50 + 150)
        nd = rotate(d, "R")
    elif p[0] == 0 and p[1] >= 150 and tuple(d) == (-1, 0):
        n = (p[1] - 150 + 50, 0)
        nd = rotate(d, "L")
    # 7
    elif p[0] >= 100 and p[1] == 0 and tuple(d) == (0, -1):
        n = (p[0] - 100, 199)
        nd = d
    elif p[1] == 199 and tuple(d) == (0, 1):
        n = (p[0] + 100, 0)
        nd = d

    try:
        n
        nd
    except UnboundLocalError:
        print(p, d)
    return n, nd


def rotate(d, ch):
    if ch == "L":
        d = R @ d
    else:
        d = (-1 * R) @ d
    return d


if __name__ == "__main__":
    p = Puzzle()
    # test = True
    test = False
    # part_one = True
    part_one = False
    d = np.array([1, 0])
    if test:
        pos = np.array([8, 0])
        data = p.load_input("input_test.txt", is_raw=True)
    else:
        pos = np.array([50, 0])
        data = p.load_input(is_raw=True)
    inst = data[-1]

    m = {}
    for j, l in enumerate(data):
        if l == "\n":
            break
        for i, ch in enumerate(l):
            if ch == "." or ch == "#":
                m[(i, j)] = ch

    inst = data[-1]
    while inst:
        g = re.match(r"(\d+)(.*)", inst)
        move = int(g.groups()[0])
        inst = g.groups()[1]
        for _ in range(move):
            new_pos = move_one(pos, d)
            if new_pos is None:
                break
            else:
                pos = new_pos

        if inst:
            ch = inst[0]
            inst = inst[1:]
            d = rotate(d, ch)
        else:
            rotate = None

    print(pos, d)
    # add +1 to pos.
    print((1 + pos[0]) * 4 + (1 + pos[1]) * 1000)
