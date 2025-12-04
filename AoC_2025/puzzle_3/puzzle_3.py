from utils.puzzle import Puzzle
import re

def find_largest(line, x):
    for n in range(x, 0, -1):
        x = re.search(str(n), line)
        if x:
            return (n, x.start())


if __name__ == '__main__':
    p = Puzzle(day=3, year=2025)
    data = p.load_input(string=True)
    # data = p.load_input('input_test.txt', string=True)

    total = 0

    for line in data:
        seq = []
        i = 0
        for q in range(11, 0, -1):
            n, j = find_largest(line[i:-q], 9)
            seq.append(str(n))
            i = i + j + 1
        n, j = find_largest(line[i:], 9)
        seq.append(str(n))
        total += int(''.join(seq))


    print(total)


