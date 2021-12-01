import copy
from parse import parse


if __name__ == "__main__":
    INPUT = []

    filename = "puzzle_2_input.txt"
    data = []

    with open(filename, "r") as input_file:
        for line in input_file:
            (i, o) = parse("{} -> {}", line.strip())
            data.append((i, o))

    # data2 = deepcopy(data)