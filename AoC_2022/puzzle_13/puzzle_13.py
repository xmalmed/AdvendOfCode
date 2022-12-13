from copy import deepcopy

from utils.puzzle import Puzzle


def is_ordered(l1, l2):
    try:
        i2 = l2.pop(0)
    except IndexError:
        return False

    try:
        i1 = l1.pop(0)
    except IndexError:
        return True

    if isinstance(i1, int) and isinstance(i2, int):
        if i1 < i2:
            return True
        elif i1 > i2:
            return False
        else:
            return None
    elif isinstance(i1, list) and isinstance(i2, int):
        i2 = [i2]
    elif isinstance(i1, int) and isinstance(i2, list):
        i1 = [i1]

    for _ in range(max(len(i1), len(i2))):
        ordered = is_ordered(i1, i2)

        if ordered is not None:
            return ordered


if __name__ == "__main__":
    p = Puzzle()
    # data = p.load_input()
    data = p.load_input('input_test.txt')
    part2_data = [eval(d) for d in data if d != '']

    index = 0
    sum_index = 0
    while data:
        index += 1
        l1 = eval(data.pop(0))
        l2 = eval(data.pop(0))
        try:
            data.pop(0)
        except IndexError:
            print('EOF')

        ordered = None
        while ordered is None:
            ordered = is_ordered(l1, l2)
            if ordered:
                sum_index += index

    print(f"Sum of ordered indexes: {sum_index}")

    # part 2
    sorted_data = [[[2]], [[6]]]
    for d in part2_data:
        s = False
        for i, sd in enumerate(sorted_data):
            if is_ordered([deepcopy(d)], [deepcopy(sd)]):
                sorted_data.insert(i, d)
                s = True
                break
        if not s:
            sorted_data.append(d)

    # print(part2_data)
    for d in sorted_data:
        print(d)
    print(f"decode: {(1+sorted_data.index([[2]]))  * (1+sorted_data.index([[6]]))}")
