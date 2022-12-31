from utils.puzzle import Puzzle
from parse import parse


if __name__ == "__main__":
    p = Puzzle(day=21)
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    remain_monkeys = data.copy()
    root = None
    while data:
        line = data.pop(0)
        m, expression = parse('{}: {}', line)
        try:
            exec(f'{m} = {expression}')
            # monkeys[m] = eval(expression)
        except NameError:
            data.append(line)

    print(f"Part 1: Monkey 'root': {root}")

