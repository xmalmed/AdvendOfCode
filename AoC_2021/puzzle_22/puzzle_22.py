from utils.puzzle import Puzzle
from parse import parse
from itertools import product


def overlap(n, o):
    if all(
            [
                o[1] <= n[1] <= o[2] or n[1] <= o[1] <= n[2] or o[1] <= n[2] <= o[2] or n[1] <= o[2] <= n[2],
                o[3] <= n[3] <= o[4] or n[3] <= o[3] <= n[4] or o[3] <= n[4] <= o[4] or n[3] <= o[4] <= n[4],
                o[5] <= n[5] <= o[6] or n[5] <= o[5] <= n[6] or o[5] <= n[6] <= o[6] or n[5] <= o[6] <= n[6],
            ]
    ):
        a = -1 * o[0]
        old = create_sets(o)
        new = create_sets(n)
        x = old[1].intersection(new[1])
        y = old[2].intersection(new[2])
        z = old[3].intersection(new[3])
        return (a, x, y, z)
    else:
        return None


def create_sets(step):
    x1 = step[1]
    x2 = step[2]
    y1 = step[3]
    y2 = step[4]
    z1 = step[5]
    z2 = step[6]
    return step[0], set(range(x1, x2 + 1)), set(range(y1, y2 + 1)), set(range(z1, z2 + 1))


if __name__ == '__main__':
    p = Puzzle(day=22, year=2021)
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    # part 2
    count = 0
    sections = []
    tt = 0
    for d in data:
        tt += 1
        a, x1, x2, y1, y2, z1, z2 = parse('{:l} x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}', d)
        a = 1 if a == 'on' else -1
        step = (a, x1, x2, y1, y2, z1, z2)
        add_sections = []
        if step[0] == 1:
            add_sections.append(step)
            count += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
            for s in sections:
                o = overlap(step, s)
                if o:
                    add_sections.append((o[0], min(o[1]), max(o[1]), min(o[2]), max(o[2]), min(o[3]), max(o[3])))
                    count += o[0] * len(o[1]) * len(o[2]) * len(o[3])
        else:
            for s in sections:
                o = overlap(step, s)
                if o:
                    add_sections.append((o[0], min(o[1]), max(o[1]), min(o[2]), max(o[2]), min(o[3]), max(o[3])))
                    count += o[0] * len(o[1]) * len(o[2]) * len(o[3])

        sections += add_sections
        print(tt, count)
    print(f"part2: {count}")

    # part 1
    cubes = {}
    count = 0
    steps = []
    for step in data:
        a, x1, x2, y1, y2, z1, z2 = parse('{:l} x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}', step)

        cuboid = product(range(max(x1, -50), min(x2, 50) + 1), range(max(y1, -50), min(y2, 50) + 1),
                         range(max(z1, -50), min(z2, 50) + 1))
        for c in cuboid:
            if a == 'on':
                cubes[c] = 1
            else:
                cubes.pop(c, None)

    print(f"part 1: {len(cubes)}")
