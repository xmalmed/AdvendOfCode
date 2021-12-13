from utils.puzzle import Puzzle
from parse import parse


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    image = {}
    for i, line in enumerate(data):
        if line == "":
            break
        x, y = (int(v) for v in line.split(","))
        image[(x, y)] = "#"

    for folding in data[i + 1 :]:
        axis, fold = parse("fold along {}={:d}", folding)
        axis = 0 if axis == "x" else 1

        new_image = {}
        for dot in image:
            if dot[axis] > fold:
                new = fold - (dot[axis] - fold)
                if axis:
                    new_image[(dot[0], new)] = "#"
                else:
                    new_image[(new, dot[1])] = "#"
            else:
                new_image[dot] = "#"
        image = new_image
        print(len(image))

    plot = []
    for _ in range(7):
        plot.append(["."] * 42)
    for position in image:
        plot[position[1]][position[0]] = "#"
    for line in plot:
        print("".join(line))
