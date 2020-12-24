from datetime import time
from bidict import bidict

input = '389125467'  # test


# input = '496138527'  # real (start only)


def run_game(cups, moves):
    mod = len(cups)
    pick = 3
    cc = 1  # current cup
    start = time()

    for j in range(1, moves + 1):
        if j % 1 == 0:
            print(f'{j / 100000} %')
        picked = []
        for i in range(1, pick + 1):
            shift = cc + i
            if shift > mod:
                shift -= mod
            picked.append(cups[shift])
        cc_value = cups[cc]
        dc_value = cc_value - 1
        if dc_value == 0:
            dc_value = mod
        while dc_value in picked:
            dc_value -= 1
            if dc_value == 0:
                dc_value = mod

        # empty picked positions
        for value in picked:
            cups[cups.inverse[value]] = -value
        dc = cups.inverse[dc_value]

        # change positions
        if dc > cc:
            for i in range(cc + 1, dc - pick + 1):
                value = cups[i + pick]
                cups[i + pick] = -1 * value  # problem with duplications
                cups[i] = value
            for j in range(pick):
                cups[dc - pick + 1 + j] = picked[j]  # safe, there are free indexes
        else:
            for i in range(cc, dc, -1):
                value = cups[i]
                cups[i] = -1 * value
                shift = i + pick
                if shift > mod:     # not safe
                    shift -= mod
                cups[shift] = value
            for j in range(pick):
                shift = dc + 1 + j
                if shift > mod:
                    shift -= mod
                cups[shift] = picked[j]

        # next cc
        cc = (cups.inverse[cc_value] + 1)
        if cc == mod + 1:
            cc = 1

    return cc, cups


# part 1
cups = bidict(zip(range(1, len(input) + 1), [int(x) for x in input]))

cc, cups = run_game(cups, 100)

print(f'final: {cups}')
# print(f'index: {cc}, value: {cups[cc]}')
# temp = ''.join(map(str, cups)).split('1')
# print(temp[1] + temp[0])

# part 2
cups = bidict(zip(range(1, 1000000 + 1), [int(x) for x in input] + list(range(len(input) + 1, 1000000 + 1))))

cc, cups = run_game(cups, 10000000)
mod = len(cups)
print(f'mod: {mod}, cc: {cc}')
c0 = cups.inverse[1]
print(f'cup 1 at: {c0}')
shift = c0 + 1
if shift > mod:
    shift -= mod
c1_value = cups[shift]
shift = c0 + 2
if shift > mod:
    shift -= mod
c2_value = cups[shift]
print(f'after cup 1: {c1} * {c2} = {c1 * c2}')
print(f'cup around 1: {cups[c0 - 3 : c0 + 4]}')
