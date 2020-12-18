from parse import parse
from pathlib import Path
from re import sub


class NewInt(int):
    def __add__(self, other):
        return NewInt(self.__int__() * other)

    def __mul__(self, other):
        return NewInt(self.__int__() + other)


# filename = "input_18_test.txt"
filename = "input_18.txt"

# part2

results2 = []
with Path(filename).open() as file:
    for line in file:
        line = line.replace('+', '#')
        line = line.replace('*', '+')
        line = line.replace('#', '*')
        new_line = sub(r'(\d+)', r'NewInt(\1)', line)
        results2.append(int(eval(new_line)))    # don't use NewInt here :D

print(sum(results2))


# part1
def evaluate_parentheses(line: str):
    try:
        idx_right = line.index(')')
    except ValueError:
        return None
    sub_rev_line = line[idx_right::-1]
    idx_left_rev = sub_rev_line.index('(')
    return len(sub_rev_line) - idx_left_rev - 1, idx_right


def solve_math(math_str: str) -> str:
    math = math_str.split(' ')
    while len(math) >= 3:
        a = int(math.pop(0))
        op = math.pop(0)
        b = int(math.pop(0))
        if op == '+':
            math.insert(0, a + b)
        else:
            math.insert(0, a * b)
    if len(math) == 2:
        print("problem!!!")
    if len(math) == 1:
        return str(math[0])


results = []
with Path(filename).open() as file:
    for line in file:
        parentheses = True
        while parentheses:
            positions = evaluate_parentheses(line)
            if positions is None:
                parentheses = False
                continue
            else:
                result = solve_math(line[positions[0] + 1: positions[1]])
                line = line[:positions[0]] + result + line[positions[1] + 1:]
        # print(solve_math(line))
        results.append(int(solve_math(line)))

print(sum(results))



