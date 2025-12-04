from utils.puzzle import Puzzle

if __name__ == '__main__':
    p = Puzzle(day=1, year=2025)
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    pos = 50
    count = 0
    for i in data:
        start_pos = pos
        value = int(i[1:])
        count += abs(value) // 100
        value %= 100
        if i.startswith('L'):
            pos -= value
            if start_pos == 0:
                count -= 1
        elif i.startswith('R'):
            pos += value
        if pos == 0:
            count += 1
        if pos >= 100 or pos < 0:
            pos %= 100
            count += 1



    print(count)