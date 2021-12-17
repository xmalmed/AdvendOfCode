from utils.puzzle import Puzzle
from parse import parse


def is_in_target(vx, vy):
    x, y = 0, 0
    while y >= -73:
        x += vx
        y += vy
        if x in X and y in Y:
            return True
        if vx > 0:
            vx -= 1
        vy -= 1
    return False


if __name__ == '__main__':
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input('input_test.txt')
    x1, x2, y1, y2 = parse('target area: x={:d}..{:d}, y={:d}..{:d}', data[0])
    X = range(x1, x2 + 1)
    Y = range(y1, y2+1)

    count = 0
    for vx in range(22, 281):
        for vy in range(-73, 73):
            if is_in_target(vx, vy):
                count += 1

    print(count)

    for i in range(40):
        print(i, ' ', i*(i+1)/2)
