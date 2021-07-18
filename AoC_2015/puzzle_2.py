# -*- coding: utf-8 -*-
"""
Created on 18. 7. 2021
@author: malmed
"""

from parse import parse


def get_sides(box):
    return (box[0] * box[1], box[1] * box[2], box[2] * box[0])


def get_surface(sides):
    return 2 * sum(sides) + min(sides)


def get_ribbon(box):
    sb = sorted(box)
    return box[0] * box[1] * box[2] + 2*(sb[0] + sb[1])


if __name__ == '__main__':
    filename = 'puzzle_2_input.txt'
    with open(filename, 'r') as data:
        boxes = []
        for line in data:
            boxes.append(parse('{:d}x{:d}x{:d}', line.strip()))

    print(
        sum(
            [get_surface(get_sides(box)) for box in boxes]
        )
    )

    print(
        sum(
            [get_ribbon(box) for box in boxes]
        )
    )
