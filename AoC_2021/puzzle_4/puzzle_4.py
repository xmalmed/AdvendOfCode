from utils.puzzle import Puzzle
from numpy import array, where, sum


def load_table(index: int):
    table = []
    for i in range(5):
        table.append([int(x) for x in data[index + i].split()])
    return array(table)


def is_bingo(n, t):
    position = where(t == n)
    if len(position[0]) > 0:
        t[position] = -1
        if any(sum(t, 0) == -5):
            return True
        if any(sum(t, 1) == -5):
            return True
    return False


def find_first_bingo():
    for n in draws:
        for t in tables:
            if is_bingo(n, t):
                t[t == -1] = 0
                print(t)
                print(f'Bingo, {n} * {sum(sum(t))} = {n * (sum(sum(t)))}')
                return


def find_last_bingo():
    for n in draws:
        for t in tables:
            if is_bingo(n, t):
                t[t == -1] = 0
                print(f'Bingo, {n} * {sum(sum(t))} = {n * (sum(sum(t)))}')
                t[t > -2] = -10


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    draws = [int(x) for x in data[0].split(",")]
    tables = []
    index = 2
    while index < len(data):
        tables.append(load_table(index))
        index += 6

    # find_first_bingo()

    print('--------')
    find_last_bingo()
