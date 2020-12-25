# -*- coding: utf-8 -*-
"""
Created on 25. 12. 2020
@author: malmed
"""
card_pub = 13233401
door_pub = 6552760
mod = 20201227  # prime number

# example
# print(7 ** 8 % mod)  # 5764801
# print(7 ** 11 % mod)  # 17807724
# print((7 ** 11 % mod) ** 8 % mod)
# value = 1
# for i in range(8):
#     value *= 17807724
#     value = value % mod
# print(value) # 14897079


def try_loop(key):
    value = 1
    loop = 0
    while True:
        loop += 1
        value *= 7
        value = value % mod
        if value == key:
            print(loop)
            return loop
        if loop % 100000 == 0:
            print(loop)


card_loop = try_loop(card_pub)  # 16679169
value = 1
for i in range(card_loop):
    value *= door_pub
    value = value % mod
print(value)
