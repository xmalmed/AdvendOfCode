from utils.puzzle import Puzzle


def get_space_value(last_space):
    if iea[0] == 0:
        return 0
    elif iea[-1] == 1:
        return 1
    else:
        return (last_space + 1) % 2


def get_number(x, y, image, default):
    num = []
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if (x + dx, y + dy) in image:
                num.append(str(image[(x + dx, y + dy)]))
            else:
                num.append(str(default))
    v = int("".join(num), 2)
    return v


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")
    iea = [1 if ch == "#" else 0 for ch in data[0]]

    images = []
    for j in range(0, 51):
        images.append({})

    for y, line in enumerate(data[2:]):
        for x, ch in enumerate(line):
            if ch == "#":
                images[0][(x, y)] = 1

    size_x = x + 1
    size_y = y + 1

    space = 0
    for i in range(1, 51):
        new_space = get_space_value(space)
        for y in range(0 - i, size_y + i):
            for x in range(0 - i, size_x + i):
                value = iea[get_number(x, y, images[i - 1], space)]
                if value != new_space:
                    images[i][(x, y)] = value
        space = new_space
        # print_test_image(image)
        if i == 3:
            print(len(images[i]))
    print(len(images[50]))
