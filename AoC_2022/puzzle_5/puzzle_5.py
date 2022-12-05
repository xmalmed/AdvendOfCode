from utils.puzzle import Puzzle
from parse import parse

if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input(raw=True)
    # data = p.load_input("input_test.txt", raw=True)

    instructions = []
    STACKS = 9
    # STACKS = 3
    stacks = [[] for _ in range(STACKS)]
    for i, line in enumerate(data):
        if line == "\n":
            instructions = data[i + 1 :]
            break
        for j in range(STACKS):
            box = line[:3]
            if box != "   ":
                stacks[j].append(box[1])
            line = line[4:]

    for s in stacks:
        s.pop(-1)

    for inst in instructions:
        c, f, t = parse("move {:d} from {:d} to {:d}", inst.strip())
        f -= 1
        t -= 1

        # part 1
        # for _ in range(c):
        #     stacks[t].insert(0, stacks[f].pop(0))

        # part 2
        stacks[t] = stacks[f][:c] + stacks[t]
        stacks[f] = stacks[f][c:]

    print("code: " + "".join([x[0] for x in stacks]))
