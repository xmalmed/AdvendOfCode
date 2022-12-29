from utils.puzzle import Puzzle
import numpy as np


class Cube:
    def __init__(self, xyz):
        self.xyz = xyz
        self.neighbours = []

    def __sub__(self, other):
        return np.subtract(self.xyz, other.xyz)

    def distance2(self, other):
        d = self - other
        dist = d[0] ** 2 + d[1] ** 2 + d[2] ** 2
        return True if dist == 1 else False

    def free_sides(self):
        return 6 - len(self.neighbours)


DIR = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]

space = np.zeros((23, 23, 23), dtype=int)
expanded = [(0, 0, 0)]


def expand(xyz):
    expanded = []
    for d in DIR:
        neighbour = tuple(np.add(xyz, d))
        try:
            if space[neighbour] == 0:
                space[neighbour] = 2
                expanded.append(neighbour)
        except IndexError:
            continue
    return expanded


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    cubes = []
    for xyz in data:
        space[eval(xyz)] = 1
        new_c = Cube(eval(xyz))
        for c in cubes:
            if new_c.distance2(c) == 1:
                new_c.neighbours.append(c)
                c.neighbours.append(new_c)

        cubes.append(new_c)

    print(f"part 1: surface is: {sum([c.free_sides() for c in cubes])}")

    while expanded:
        new_expand = expand(expanded.pop())
        expanded += new_expand

    exposed_sides = 0
    for i in range(22):
        for j in range(22):
            for k in range(22):
                if space[i, j, k] == 1:
                    for d in DIR:
                        check = tuple(np.add((i, j, k), d))
                        try:
                            if space[check] == 2:
                                exposed_sides += 1
                        except IndexError:
                            continue

    print(f"Part 2: exposed sides: {exposed_sides}")
