# -*- coding: utf-8 -*-
"""
Created on 30. 11. 2021
@author: malmed
"""
import copy

from parse import parse


def try_operation(ii, o):
    if len(ii) == 1:
        # a -> b
        try:
            wires[o] = int(ii[0])
        except ValueError:
            wires[o] = wires[ii[0]]
    elif len(ii) == 2:
        # NOT
        wires[o] = 65535 - wires[ii[1]]
    else:
        if ii[1] == "AND":
            try:
                wires[o] = int(ii[0]) & wires[ii[2]]
            except ValueError:
                wires[o] = wires[ii[0]] & wires[ii[2]]

        elif ii[1] == "OR":
            try:
                wires[o] = int(ii[0]) | wires[ii[2]]
            except ValueError:
                wires[o] = wires[ii[0]] | wires[ii[2]]

        elif ii[1] == "LSHIFT":
            wires[o] = wires[ii[0]] << int(ii[2])

        elif ii[1] == "RSHIFT":
            wires[o] = wires[ii[0]] >> int(ii[2])

    return True


if __name__ == "__main__":

    filename = "puzzle_7_input.txt"
    wires = {}
    data = []

    with open(filename, "r") as man:
        for line in man:
            (i, o) = parse("{} -> {}", line.strip())
            # print(i, " xxxxxxx ", o)
            ii = i.split()
            data.append((ii, o))

    data2 = copy.deepcopy(data)

    while data:
        for d in data:
            try:
                r = try_operation(d[0], d[1])
            except KeyError:
                continue
            if r:
                data.remove(d)
            r = False

    print("Wire 'a' has value:", wires["a"])

    # part 2
    for i, d in enumerate(data2):
        if d[1] == 'b':
            data2[i] = ([wires['a'], ], 'b')
    wires = {}

    while data2:
        for d in data2:
            try:
                r = try_operation(d[0], d[1])
            except KeyError:
                continue
            if r:
                data2.remove(d)
            r = False

    print("New Wire 'a' has value:", wires["a"])
