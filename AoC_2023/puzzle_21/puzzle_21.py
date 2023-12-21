from utils.puzzle import Puzzle

if __name__ == '__main__':
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input('input_test.txt')
    # S = 64
    # S = 6
    S = 5000
    # S = 26501365

    g = {}

    for y, l in enumerate(data):
        for x, ch in enumerate(l):
            g[(y, x)] = ch
            if ch == 'S':
                origin = (y, x)
                g[(y, x)] = 0

    print(origin)
    last = [origin]
    for i in range(1, S+1):
        print(i)
        print()
        new_last = []
        color = i % 2
        for y, x in last:
            xp = x + 1
            xm = x - 1
            yp = y + 1
            ym = y - 1
            if g[(y, xp)] == '.':
                g[(y, xp)] = color
                new_last.append((y, xp))
            if g[(y, xm)] == '.':
                g[(y, xm)] = color
                new_last.append((y, xm))
            if g[(yp, x)] == '.':
                g[(yp, x)] = color
                new_last.append((yp, x))
            if g[(ym, x)] == '.':
                g[(ym, x)] = color
                new_last.append((ym, x))
        last = new_last


    results = [k for k, v in g.items() if v == 0]
    # print(results)
    print(len(results))

