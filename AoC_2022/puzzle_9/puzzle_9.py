from utils.puzzle import Puzzle
import numpy as np


def update_tail(tail, head):
    vx, vy = tuple(np.subtract(head, tail))
    dx = 0
    dy = 0
    if abs(vx) > 1 or abs(vy) > 1:
        dx = vx
        dy = vy
        if abs(vx) > 1:
            dx = np.sign(vx)
        if abs(vy) > 1:
            dy = np.sign(vy)
    return (tail[0] + dx, tail[1] + dy)


if __name__ == '__main__':
    p = Puzzle()
    data = p.load_input(string=True)
    # data = p.load_input('input_test.txt', string=True)

    knots = {i: (0, 0) for i in range(10)}
    grid1 = {knots[1]: 1}
    grid9 = {knots[9]: 1}

    for operation in data:
        direction, moves = operation.split(' ')
        match direction:
            case 'U':
                d = (0, 1)
            case 'D':
                d = (0, -1)
            case 'L':
                d = (-1, 0)
            case 'R':
                d = (1, 0)

        for _ in range(int(moves)):
            knots[0] = tuple(np.add(knots[0], d))

            for i in range(1, 10):
                knots[i] = update_tail(knots[i], knots[i-1])
            grid1[knots[1]] = 1
            grid9[knots[9]] = 1

    print(f"The first knot visited {len(grid1)}")
    print(f"The last knot visited {len(grid9)}")
