from utils.puzzle import Puzzle
from parse import parse
from itertools import product


if __name__ == '__main__':
    p = Puzzle(day=22, year=2021)
    # data = p.load_input()
    data = p.load_input('input_test.txt')

    cubes = {}
    count = 0
    steps = []
    for step in data:
        a, x1, x2, y1, y2, z1, z2 = parse('{:l} x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}', step)

        cuboid = product(range(max(x1, -50), min(x2, 50) +1 ), range(max(y1, -50), min(y2, 50) +1), range(max(z1, -50), min(z2, 50)+1))
        for c in cuboid:
            if a == 'on':
                cubes[c] = 1
            else:
                cubes.pop(c, None)


        # for s in steps:
        #     if s[1] <= x1 <= s[2] or s[1] <= x2 <= s[2]:
        #         if s[3] <= y1 <= s[4] or s[3] <= y2 <= s[4]:
        #             if s[5] <= z1 <= s[6] or s[5] <= z2 <= s[6]:
        #                 if s[0] == 'on':
        #                     # minus
        #                 if
        # if a == 'on':
        #     count += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 +1)
        #     steps.append((a, x1, x2, y1, y2, z1, z2))



        # steps.append((s, x1, x2, y1, y2, z1, z2))




    print(f"part 1: {len(cubes)}")

