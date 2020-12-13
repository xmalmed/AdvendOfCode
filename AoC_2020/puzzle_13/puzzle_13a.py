DEP = 1009310
LINES = [19, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 37, 'x', 'x', 'x', 'x', 'x', 599, 'x', 29, 'x',
         'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 17, 'x', 'x', 'x', 'x', 'x', 23, 'x', 'x',
         'x', 'x', 'x', 'x', 'x', 761, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 41, 'x', 'x', 13]

# buses except 599, 761
BUSES = [19, 37, 29, 17, 23, 41, 13]

# diff from 599
DIFFS = [-19, -6, 2, 17, 23, 41, 44]


def try_next(n: int, first, second, start):
    return first * (start + (n * second))


# print(solve(599, 761, 31))  # => 174, 137
n = 3000000000
# until_true = True
while True:
    n += 1
    if n % 100 == 0:
        print(n)
    time = try_next(n, 599, 761, 174)
    if (time - 19) % 19 == 0 and (time - 6) % 37 == 0 and (time + 2) % 29 == 0 and (time + 17) % 17 == 0 and (
            time + 23) % 23 == 0 and (time + 41) % 41 == 0 and (time + 44) % 13 == 0:
        print(time - 19)
        break


def solve(x: int, y: int, z: int):
    modus = abs(y - x)
    if x < y:
        zz = -z % modus
        xx = (x % modus)
        for c in range(modus):
            if (c * xx) % modus == zz:
                b = (c * x + z) / (y - x)
                return b + c, b
    else:
        x, y = y, x
        z = -z
        zz = -z % modus
        xx = (x % modus)
        for c in range(1, modus + 1):
            if (c * xx) % modus == zz:
                b = (c * x + z) / (y - x)
                return b, b + c


# print(solve(19, 37, 13))  # => 11, 6
# print(solve(19, 599, 19))  # => 598 19
# print(solve(19, 29, 21))  # => 5 4
# print(solve(19, 17, 36))  # => 16 20
# print(solve(19, 23, 42))  # => 22 20
# print(solve(19, 761, 50))  # => 478 12
# print(solve(19, 41, 60))  # => 40 20
# print(solve(19, 13, 63))  # => 9, 18

# print(solve(37, 599, -587))  # => 113, 6
# print(solve(19, 37, -1))  # => 113, 6


# tests
# print(solve(7, 13, 1))  # => 11, 6
# print(solve(3, 5, 1))  # => 3, 2
# print(solve(19, 37, 13))  # => 11, 6
# print(solve(37, 19, -13))  # => 6, 11
# print(solve(5, 3, 1))  # => 1, 2
# print(solve(1789, 37, 1))  # => 17, 822

# TEST1 = [17, 'x', 13, 19]
# print(solve(17, 13, 2))
# print(solve(17, 19, 3))
# print(solve(13, 19, 1))
# print(solve(13, 19, -5))


# part 1
# lines = [num for num in LINES if isinstance(num, int)]
#
# times = []
# for bus in lines:
#     times.append(bus - (DEP % bus))
#
# print(lines)
# print(times)
# print(599 * 5)


# EXAPMLE
BUSES2 = [37, 47]
DIFFS2 = [1, 2]
# print(solve(1789, 1889, 3))  # => 1379, 1306
# start 1379 * 1789 = 2467031
# n = 0
# while True:
#     n += 1
#     print(n)
#     time = try_next(n, 1789, 1889, 1379)
#     if (time + 1) % 37 == 0 and (time + 2) % 47 == 0:
#         print(time)
#         break
#
