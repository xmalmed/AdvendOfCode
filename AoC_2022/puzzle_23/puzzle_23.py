from utils.puzzle import Puzzle


def run_round(elfs, directions):
    m = []
    for y, x in elfs.keys():
        moving = False
        for dy, dx in around:
            if (y + dy, x + dx) in elfs:
                moving = True
        if moving:
            for d in directions:
                moving2 = True
                for dy, dx in d:
                    if (y + dy, x + dx) in elfs:
                        moving2 = False
                if moving2:
                    move = [(y, x), (y + d[1][0], x + d[1][1])]
                    m.append(move)
                    break

    # remove duplicate move
    m.sort(key=lambda elf: elf[1])
    mm = []
    while m:
        e = m.pop(0)
        if len(m) == 0:
            mm.append(e)
        else:
            if e[1] == m[0][1]:
                m.pop(0)
            else:
                mm.append(e)

    # change positions:
    if mm == []:
        return False

    for e, m in mm:
        del elfs[e]
        elfs[m] = 1

    return elfs


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")
    rounds = 10
    directions = [
        [(-1, -1), (-1, 0), (-1, 1)],
        [(1, -1), (1, 0), (1, 1)],
        [(-1, -1), (0, -1), (1, -1)],
        [(-1, 1), (0, 1), (1, 1)],
    ]
    around = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]

    elfs = {}

    for y, l in enumerate(data):
        for x, ch in enumerate(l):
            if ch == "#":
                elfs[(y, x)] = 1

    # for i in range(rounds):
    #     print(i)
    #     run_round(elfs, directions)
    #     # rotate directions
    #     d = directions.pop(0)
    #     directions.append(d)
    #     print()
    #
    # xx = sorted([x for x, y in elfs])
    # yy = sorted([y for x, y in elfs])
    # print('empty spaces')
    # print( (xx[-1] - xx[0] + 1) * (yy[-1] - yy[0] + 1) - len(elfs) )

    is_moving = True
    round = 0
    while is_moving:
        round += 1
        print(round)
        elfs = run_round(elfs, directions)
        if elfs is False:
            is_moving = False
        # rotate directions
        d = directions.pop(0)
        directions.append(d)

    print(f'round: {round}')
