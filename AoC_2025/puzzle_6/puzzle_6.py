from utils.puzzle import Puzzle
import math

if __name__ == '__main__':
    p = Puzzle(day=6, year=2025)
    data = p.load_input(is_raw=True)
    # data = p.load_input('input_test.txt', is_raw=True)

    numbers = []
    for line in data:
        l = line.strip()
        for _ in range(4):
            l = l.replace('  ', ' ')
        try:
            num = [int(n) for n in l.split(' ')]
        except ValueError:
            num = l.split(' ')
        numbers.append(num)

    problems = zip(*numbers)

    total = 0
    for p in problems:
        if p[-1] == '*':
            total += math.prod(p[:-1])
        else:
            total += sum(p[:-1])

    print(total)

    # ==============
    problems2 = zip(*data[:-1])
    operators = numbers[-1]
    prob = []
    total2 = 0
    for x in problems2:
        if set(x) == {' '}:
            op = operators.pop(0)
            if op == '+':
                total2 += sum(prob)
            elif op == '*':
                total2 += math.prod(prob)
            prob = []
            continue
        try:
            prob.append(int(''.join(x)))
        except ValueError:
            pass

    op = operators.pop(0)
    if op == '+':
        total2 += sum(prob)
    elif op == '*':
        total2 += math.prod(prob)
    prob = []

    print(total2)


