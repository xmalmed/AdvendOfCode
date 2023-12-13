from utils.puzzle import Puzzle

def move_right(m):
    move1 = []
    for k, v in m.items():
        if v == '>':
            try:
                if m[(k[0], k[1] + 1)] == '.':
                    move1.append(k)
            except KeyError:
                if m[(k[0], 0)] == '.':
                    move1.append(k)

    for i, j in move1:
        try:
            m[(i, j + 1)]
            m[(i, j + 1)] = m[(i, j)]
        except KeyError:
            m[(i, 0)] = m[(i, j)]
        m[(i, j)] = '.'

    return move1


def move_down(m):
    move1 = []
    for k, v in m.items():
        if v == 'v':
            try:
                if m[(k[0] + 1, k[1])] == '.':
                    move1.append(k)
            except KeyError:
                if m[(0, k[1])] == '.':
                    move1.append(k)

    for i, j in move1:
        try:
            m[(i + 1, j)]
            m[(i + 1, j)] = m[(i, j)]
        except KeyError:
            m[(0, j)] = m[(i, j)]
        m[(i, j)] = '.'

    return move1

def mprint(m):
    for i in range(9):
        s = ''
        for j in range(10):
            s = s + m[(i,j)]
        print(s)


if __name__ == '__main__':
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    m = {}
    for i, r in enumerate(data):
        for j, ch in enumerate(r):
            m[(i, j)] = ch

    cycles = 0
    move1 = move2 = [1]
    mprint(m)
    while move1 != [] or move2 != []:
        cycles += 1
        print(cycles)
        move1 = move_right(m)
        move2 = move_down(m)
        mprint(m)
        print()

    print(cycles)