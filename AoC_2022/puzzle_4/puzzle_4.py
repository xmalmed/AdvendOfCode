from utils.puzzle import Puzzle
from parse import parse


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    count = 0
    count2 = 0
    for line in data:
        a1, a2, b1, b2 = parse("{:d}-{:d},{:d}-{:d}", line)
        sa = set(range(a1, a2+1))
        sb = set(range(b1, b2+1))
        la = len(sa)
        lb = len(sb)
        lu = len(sa.union(sb))
        if lu == max(la, lb):
            count += 1
            count2 += 1
        elif lu < (la + lb):
            count2 += 1

    print(f"Part 1: full overlaps {count}")
    print(f"Part 2: any overlaps: {count2}")