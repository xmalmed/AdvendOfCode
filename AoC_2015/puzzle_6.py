# -*- coding: utf-8 -*-
"""
Created on 2. 8. 2021
@author: malmed
"""

import hashlib
import numpy as np
from parse import parse
import re


def turn_on(x1, y1, x2, y2):
    lights[x1:x2, y1:y2] = abs(lights[x1:x2, y1:y2])


def turn_off(x1, y1, x2, y2):
    lights[x1:x2, y1:y2] = abs(lights[x1:x2, y1:y2]) * -1


def toggle(x1, y1, x2, y2):
    lights[x1:x2, y1:y2] = lights[x1:x2, y1:y2] * -1


def turn_on2(x1, y1, x2, y2):
    lights[x1:x2, y1:y2] = lights[x1:x2, y1:y2] + 1


def turn_off2(x1, y1, x2, y2):
    subarray = lights[x1:x2, y1:y2] - 1
    subarray[subarray < 0] = 0
    lights[x1:x2, y1:y2] = subarray


def toggle2(x1, y1, x2, y2):
    lights[x1:x2, y1:y2] = lights[x1:x2, y1:y2] + 2


if __name__ == '__main__':
    filename = 'puzzle_6_input.txt'
    lights = np.zeros((1000, 1000), dtype=int) - 1

    with open(filename, 'r') as textfile:
        for line in textfile:
            data = parse('{action} {x1:d},{y1:d} through {x2:d},{y2:d}', line.strip())
            if data['action'] == 'turn on':
                turn_on(data['x1'], data['y1'], data['x2'] + 1, data['y2'] + 1)
            if data['action'] == 'turn off':
                turn_off(data['x1'], data['y1'], data['x2'] + 1, data['y2'] + 1)
            if data['action'] == 'toggle':
                toggle(data['x1'], data['y1'], data['x2'] + 1, data['y2'] + 1)

    print(sum(sum((lights + 1))) / 2)

    lights = np.zeros((1000, 1000), dtype=int)

    with open(filename, 'r') as textfile:
        for line in textfile:
            data = parse('{action} {x1:d},{y1:d} through {x2:d},{y2:d}', line.strip())
            if data['action'] == 'turn on':
                turn_on2(data['x1'], data['y1'], data['x2'] + 1, data['y2'] + 1)
            if data['action'] == 'turn off':
                turn_off2(data['x1'], data['y1'], data['x2'] + 1, data['y2'] + 1)
            if data['action'] == 'toggle':
                toggle2(data['x1'], data['y1'], data['x2'] + 1, data['y2'] + 1)

    print(sum(sum(lights)))
