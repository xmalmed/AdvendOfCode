from utils.puzzle import Puzzle
from parse import parse
import re

def replace_line(m, e, data):
    for i, l in enumerate(data):
        if m in l:
            new_line = l.replace(m, f"( {e} )")
            data[i] = new_line
            return


if __name__ == "__main__":
    p = Puzzle(day=21)
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    # remain_monkeys = data.copy()
    # root = None
    # while data:
    #     line = data.pop(0)
    #     m, expression = parse('{}: {}', line)
    #     try:
    #         exec(f'{m} = {expression}')
    #         # monkeys[m] = eval(expression)
    #     except NameError:
    #         data.append(line)
    #
    # print(f"Part 1: Monkey 'root': {root}")

    for i, line in enumerate(data):
        if line.startswith('root'):
            new_line = line.replace('+', '=')
            data.pop(i)
            data.append(new_line)
            break

    while len(data) > 1:
        line = data.pop(0)
        if line.startswith('humn'):
            continue

        m, expression = parse('{}: {}', line)
        replace_line(m, expression, data)

    a, b = data[0].split('=')
    _, a = a.split(':')
    root = eval(b)
    print( root )

    x = re.sub(r'\( (\d+) \)', r'\1', a)
    for _ in range(1000):
        y = re.search(r'\( \d+ [-+*/] \d+ \)', x)
        if y:
            x = x.replace(y[0], str(int(eval(y[0]))))
        else:
            break

    print(x)


20*(((7430909554588-((((((219+(2*(((((((((((599+((2*(278+(((2*((3*(((569+(((((135+(((10*(((446+(2*(((((((563+((((((((301+(((((7*(109+((116+(343+((x-838)*17)))/5)))-797)+909)/2)+636))/3)-518)*8)+294)*2)-460)/4))/3)-159)*5)-282)/2)+297)))/8)-24))-930)/2))*2)-453)+310)+24))/5)+350))-732))+711)/3)))-309))/6)-300)/12)+825)*67)-458)/2)+400)*2)-869)))/7)+22)*2)-738)/10))/4)+358)
301+(((((7*(109+((116+(343+((x-838)*17)))/5)))-797)+909)/2)+636) = 42348706938012