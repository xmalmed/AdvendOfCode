import copy
from parse import parse
from utils.puzzle import Puzzle


def find_main_bit(index: int, data: list, most=True):
    size = len(data)
    transpose_data = list(zip(*[list(d) for d in data]))
    ones = transpose_data[index].count('1')
    if ones >= size / 2:
        res = 1
    else:
        res = 0
    return str(res) if most else str((res + 1) % 2)


if __name__ == "__main__":
    p = Puzzle()
    # data = p.load_input(string=True, filename='test_input.txt')
    data = p.load_input(string=True)
    size = len(data)

    # part 1
    transpose_data = zip(*[list(d) for d in data])
    ones = [1 if td.count('1') > size / 2 else 0 for td in transpose_data]
    gamma = int(''.join([str(n) for n in ones]), 2)
    epsilon = gamma ^ (2 ** len(ones) - 1)

    print(f'{gamma} * {epsilon} = {gamma * epsilon}')

    # part 2
    data1 = copy.deepcopy(data)
    data2 = copy.deepcopy(data)
    round = 0
    while len(data1) > 1:
        v = find_main_bit(round, data1)
        data1 = [d for d in data1 if d[round] == v]
        round += 1

    oxygen = int("".join([str(n) for n in data1[0]]), 2)
    print(f'last: {data1}, => {oxygen}')

    round = 0
    while len(data2) > 1:
        v = find_main_bit(round, data2, most=False)
        data2 = [d for d in data2 if d[round] == v]
        round += 1

    co2 = int("".join([str(n) for n in data2[0]]), 2)
    print(f'last: {data2}, => {co2}')

    print(f'oxygen * co2 = {oxygen * co2}')
