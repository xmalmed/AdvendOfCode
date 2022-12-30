from utils.puzzle import Puzzle

MINUS = {(3, 0): 1, (4, 0): 1, (5, 0): 1, (6, 0): 1}
PLUS = {(4, 0): 1, (3, 1): 1, (4, 1): 1, (5, 1): 1, (4, 2): 1}
L = {(3, 0): 1, (4, 0): 1, (5, 0): 1, (5, 1): 1, (5, 2): 1}
I = {(3, 0): 1, (3, 1): 1, (3, 2): 1, (3, 3): 1}
SQUARE = {(3, 0): 1, (3, 1): 1, (4, 0): 1, (4, 1): 1}
TYPES = [MINUS, PLUS, L, I, SQUARE]

COUNT = 2022
PERIOD_TOP = 2647
PERIOD_COUNT = 1730


def down(rock):
    new_rock = {}
    for key in rock:
        new_rock[(key[0], key[1] - 1)] = 1
    if colide(new_rock):
        return False
    else:
        return new_rock


def move(rock, ch):
    new_rock = {}
    if ch == "<":
        ch = -1
    elif ch == ">":
        ch = 1
    else:
        print(f"Strange char {ch}")
    for key in rock:
        new_rock[(key[0] + ch, key[1])] = 1
    if colide(new_rock):
        return rock
    else:
        return new_rock


def colide(rock):
    for key in rock:
        if key in pit:
            return True
    else:
        return False


def add_new_rock(count, top):
    rock = TYPES[count % len(TYPES)]
    return {(k[0], k[1] + top + 4) for k in rock}


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")
    data = list(data[0])
    step = 0

    PIT = 600000
    COUNT2 = ((1000000000000 - 1723) % PERIOD_COUNT) + 1723

    pit = {
        **{(x, 0): 1 for x in range(9)},
        **{(0, y): 1 for y in range(1, PIT)},
        **{(8, y): 1 for y in range(1, PIT)},
    }
    top = 0

    period_tops = []  # = MAGIC

    for count_rocks in range(COUNT2):
        if count_rocks % 10000 == 0:
            print(count_rocks)
        rock = add_new_rock(count_rocks, top)
        falling = True

        while falling:
            rock = move(rock, data[step])
            step = (step + 1) % len(data)
            falling = down(rock)
            if falling:
                rock = falling
            else:
                pit.update(rock)
                top = max(top, max((k[1] for k in rock)))
            if step == 0:
                period_tops.append(top-sum(period_tops))
                print(period_tops)
                print(count_rocks)


        if count_rocks == COUNT - 1:
            print(f"Part 1: Total height: {top}")

    print(f"Part 2: Total height: {top + ((1000000000000 - 1723) // PERIOD_COUNT) * PERIOD_TOP}")






