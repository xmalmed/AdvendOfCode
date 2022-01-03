from utils.puzzle import Puzzle
import re

# def add_numbers(number1, number2):
#     return f'[{number1},{number2}]'


def left_right_number(text):
    nests = 0
    for i, ch in enumerate(text):
        if ch == "[":
            nests += 1
            # if nests == 5:
            #     explode = re.match(r'([0-9]+),([0-9]+)', raw_number[i+1:])
            #     explode_l = int(explode[0])
            #     explode_r = int(explode[1])
            #     left = re.match(r'.*[,\[\]]([0-9]+)', raw_number[:i])
            #     if left:
            #         left_l = int(left[1])
            #         left_part = raw_number[:left.start(1)] + str(explode_l + left_l) +
            #
            if nests > 5:
                print(text)
        elif ch == "]":
            nests -= 1
        elif ch == "," and nests == 1:
            return text[1:i], text[i + 1 : -1]


def parse_sn(text, parent):
    sn = SnailfishNumber(parent)
    left, right = left_right_number(text)
    if len(left) != 1:
        sn.left = parse_sn(left, sn)
    else:
        sn.left = int(left)

    if len(right) != 1:
        sn.right = parse_sn(right, sn)
    else:
        sn.right = int(right)
    return sn


class SnailfishNumber:
    def __init__(self, parent, left=None, right=None):
        self.left = left
        self.right = right
        self.parent = parent


    # def max_
    # def explode(self):




if __name__ == "__main__":
    p = Puzzle()
    # data = p.load_input()
    data = p.load_input("input_test.txt")

    sn_list = []
    for text in data:
        sn_list.append(parse_sn(text, None))

    for right in sn_list[1:]:
        left = sn_list[0]
        new_sn = SnailfishNumber(None)
        left.parent = new_sn
        right.parent = new_sn
        new_sn.left = left
        new_sn.right = right
        sn_list[0] = new_sn

        # TODO explode, split


