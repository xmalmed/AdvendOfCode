from utils.puzzle import Puzzle
import re

if __name__ == '__main__':
    p = Puzzle(day=7, year=2025)
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    n = len(data[0])
    star = data.pop(0)
    beam = [0] * n
    index = re.search('S', star).start()
    assert star[index] == 'S'
    beam[index] = 1
    count_splitting = 0
    for line in data:
        new_beam = [0] * n
        for i, ch in enumerate(line):
            if ch == '^' and beam[i] != 0:
                new_beam[i-1] += beam[i]
                new_beam[i+1] += beam[i]
                count_splitting += 1
        for i, ch in enumerate(beam):
            if ch != 0 and line[i] == '.':
                new_beam[i] += beam[i]
        beam = new_beam

    print(count_splitting)
    print(sum(beam))