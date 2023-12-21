from utils.puzzle import Puzzle


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    data = p.load_input("input_test.txt")
    rounds = 10
    directions = [
        [(-1, -1), (-1, 0), (-1, 1)],
        [(1, -1), (1, 0), (1, 1)],
        [(-1, -1), (0, -1), (1, -1)],
        [(-1, 1), (0, 1), (1, 1)],
    ]
    around = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]

    elfs = {}

    for y, l in enumerate(data):
        for x, ch in enumerate(l):
            if ch == "#":
                elfs[(y, x)] = 1

    m = []
    for y, x in elfs.keys():
        moving = False
        for dy, dx in around:
            if (y+dy, x + dx) in elfs:
                moving = True
        if moving:
            for d in directions:
                moving2 = True
                for dy, dx in d:
                    if (y+dy, x +dx) in elfs:
                        moving2 = False
                if moving2:
                    move = [(y, x), (y+d[1][0], x + d[1][1])]
                    m.append(move)
                    break

    # rotate directions

