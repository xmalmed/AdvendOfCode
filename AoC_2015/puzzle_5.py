# -*- coding: utf-8 -*-
"""
Created on 30. 7. 2021
@author: malmed
"""

import hashlib
from re import match
import re


def vow(text):
    vowels = 0
    for v in text:
        if v in 'aeiou':
            vowels += 1
    return True if vowels >= 3 else False


def twice(text):
    prev = ''
    for l in text:
        if l == prev:
            return True
        prev = l
    return False


def forbid(text):
    forbidden = ['ab', 'cd', 'pq', 'xy']
    for f in forbidden:
        if f in text:
            return False
    return True


# part 2
def double_twice(text):
    return re.search(r'(..).*(\1)', text)


def twice_with_space(text):
    return re.search(r'(.).\1', text)


if __name__ == '__main__':
    nice1 = 0
    nice2 = 0
    filename = 'puzzle_5_input.txt'
    with open(filename, 'r') as textfile:
        for text in textfile:
            if vow(text) and twice(text) and forbid(text):
                nice1 += 1
            if double_twice(text) and twice_with_space(text):
                nice2 += 1

    print(nice1)
    print(nice2)
