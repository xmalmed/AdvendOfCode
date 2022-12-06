from utils.puzzle import Puzzle


def find_mark(n, data):
    for i in range(n, len(data)):
        mark = set(data[i - n: i])
        if len(mark) == n:
            return i
    return False


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()[0]
    # data = p.load_input("input_test.txt")[0]

    part1 = find_mark(4, data)
    print(f'Mark 1 at: {part1}')

    part2 = find_mark(14, data)
    print(f'Mark 2 at: {part2}')
