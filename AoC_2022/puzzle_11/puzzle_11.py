from utils.puzzle import Puzzle
from parse import parse
from math import prod


class Monkey:
    def __init__(self, items, operation, test, true_monkey, false_monkey):
        self.inspect = 0
        self.items = items
        self.operation = operation
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey


if __name__ == '__main__':
    p = Puzzle()
    data = p.load_input(string=True)
    # data = p.load_input('input_test.txt', string=True)

    monkeys = []
    for n in range(0, len(data), 7):
        items = data[n + 1].split(':')[1]
        items = [int(i) for i in items.split(',')]
        op = data[n + 2].split('=')[1].strip()
        test = parse('Test: divisible by {:d}', data[n + 3])[0]
        true_m = parse('If true: throw to monkey {:d}', data[n + 4])[0]
        false_m = parse('If false: throw to monkey {:d}', data[n + 5])[0]
        monkeys.append(Monkey(items, op, test, true_m, false_m))

    divide = prod([m.test for m in monkeys])

    # for r in range(1, 21): # part 1
    for r in range(1, 10_001):
        print(r)
        for m in monkeys:
            while m.items:
                old = m.items.pop(0)
                m.inspect += 1
                # new = eval(m.operation) // 3  #part 1
                new = eval(m.operation) % divide
                if new % m.test:
                    monkeys[m.false_monkey].items.append(new)
                else:
                    monkeys[m.true_monkey].items.append(new)

    print(f"Monkeys activity: {', '.join([str(a.inspect) for a in monkeys])}")
