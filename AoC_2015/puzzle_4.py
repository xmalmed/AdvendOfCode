# -*- coding: utf-8 -*-
"""
Created on 30. 7. 2021
@author: malmed
"""

import hashlib
from re import match

if __name__ == '__main__':
    secret = 'bgvyzdsv'
    # test_secret = 'abcdef609043'
    # print(hashlib.md5(b'abcdef609043').hexdigest())

    i = 0
    while True:
        i += 1
        hash = hashlib.md5(f'{secret}{i}'.encode())
        print(i)
        if match('000000', hash.hexdigest()):
            break

    print(hash.hexdigest())

