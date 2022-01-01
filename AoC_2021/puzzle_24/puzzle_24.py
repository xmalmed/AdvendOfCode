from utils.puzzle import Puzzle


def run_code(input):
    mem = {"w": 0, "x": 0, "y": 0, "z": 0}
    for line in program:
        if line[0] == "inp":
            mem[line[1]] = int(input.pop(0))
        else:
            value = mem[line[2]] if line[2] in mem else int(line[2])
            if line[0] == "add":
                mem[line[1]] += value
            elif line[0] == "mul":
                mem[line[1]] *= value
            elif line[0] == "div":
                mem[line[1]] = mem[line[1]] // value
            elif line[0] == "mod":
                mem[line[1]] = mem[line[1]] % value
            elif line[0] == "eql":
                mem[line[1]] = 1 if mem[line[1]] == value else 0
    return mem


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    program = [line.split() for line in data]

    for number in range(91_398_299_698_996, 11_111_111_111_111, -1):
        input = list(str(number))
        if "0" in input:
            continue
        else:
            print(number)
            mem = run_code(input)
            if mem["z"] == 0:
                print(number)
                print(mem)
                break

    for number in range(41_171_183_141_291, 91_398_299_698_998, 1):
        input = list(str(number))
        if "0" in input:
            continue
        else:
            print(number)
            mem = run_code(input)
            if mem["z"] == 0:
                print(number)
                print(mem)
                break
