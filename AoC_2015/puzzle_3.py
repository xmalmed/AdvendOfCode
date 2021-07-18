# -*- coding: utf-8 -*-
"""
Created on 18. 7. 2021
@author: malmed
"""

from collections import defaultdict


def move(step, position):
    if step == '^':
        return (position[0] + 1, position[1])
    if step == 'v':
        return (position[0] - 1, position[1])
    if step == '<':
        return (position[0], position[1] - 1)
    return (position[0], position[1] + 1)


if __name__ == '__main__':
    filename = 'puzzle_3_input.txt'
    with open(filename, 'r') as file:
        directions = file.read().strip()

    grid = defaultdict(lambda: 0)
    grid[(0, 0)] = 2
    position1 = (0, 0)
    position2 = (0, 0)
    for i, step in enumerate(directions):
        if i % 2 == 1:
            position1 = move(step, position1)
            grid[position1] += 1
        else:
            position2 = move(step, position2)
            grid[position2] += 1

    print(len(grid))
