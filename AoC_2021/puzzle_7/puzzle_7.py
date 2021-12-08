from utils.puzzle import Puzzle
import numpy as np


def fuel_consumption(p: int):
    return sum([abs(p - c) for c in crabs])


def fuel_consumption2(p: int):
    return sum([abs(p - c) * (abs(p - c) + 1) / 2 for c in crabs])


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    crabs = np.array(list(map(int, data[0].split(","))))

    best = float("inf")
    best2 = float("inf")
    for p in range(min(crabs), max(crabs)):
        consumption = fuel_consumption(p)
        consumption2 = fuel_consumption2(p)
        if consumption < best:
            best = consumption
        if consumption2 < best2:
            best2 = consumption2

    print(best)
    print(best2)
