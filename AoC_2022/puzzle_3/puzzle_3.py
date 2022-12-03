from utils.puzzle import Puzzle


def priority(x):
    if ord(x) < 93:
        return ord(x) - 65 + 27
    else:
        return ord(x) - 97 + 1


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    total = 0
    total2 = 0
    b1 = 0
    b2 = 0
    for i, backpack in enumerate(data):
        b1 = b2
        b2 = b3
        b3 = backpack
        c1 = set(backpack[:len(backpack)//2])
        c2 = set(backpack[len(backpack)//2:])
        x = c1.intersection(c2).pop()
        if (i + 1) % 3 == 0:
            y = set(b1).intersection(set(b2)).intersection(set(b3)).pop()
            total2 += priority(y)
        total += priority(x)


    print(f"Part 1: total score: {total}")
    print(f"Part 2: total score: {total2}")
