from parse import parse
from numpy import array


if __name__ == "__main__":
    INPUT = []

    filename = "puzzle_2_input.txt"
    data = []

    with open(filename, "r") as input_file:
        for line in input_file:
            (d, n) = parse("{} {:d}", line.strip())
            data.append((d, n))

    print("total forward is: ", f := sum(n[1] for n in filter(lambda x: x[0] == "forward", data)))
    print(
        "total depth is: ",
        d := sum(n[1] for n in filter(lambda x: x[0] == "down", data))
        - sum(n[1] for n in filter(lambda x: x[0] == "up", data)),
    )
    print("multiply:", d*f)

    # part 2
    aim = 0
    position = array([0, 0])
    for i in data:
        if i[0] == "forward":
            position += array([i[1], i[1] * aim])
        elif i[0] == "up":
            aim -= i[1]
        elif i[0] == "down":
            aim += i[1]

    print("new position is: ", position)
    print("mutliply: ", position[0] * position[1])
