from math import gcd, atan, pi
import numpy as np

# (0, 0) top left, (x, y)
mapa = {}

with open("10_input1.txt", 'r') as f:
    input_lines = f.read().splitlines()

for i, line in enumerate(input_lines):
    for j, char in enumerate(line):
        mapa[(j, i)] = char

max_x = j
max_y = i

asteroids = [coordinate for coordinate, char in mapa.items() if char == '#']
results = []


def is_view_clear(coord1, coord2, mapa):
    x = coord1[0] - coord2[0]
    y = coord1[1] - coord2[1]
    d = gcd(abs(x), abs(y))
    x_step = x / d
    y_step = y / d
    view_is_clear = True
    step = 1
    while coord2[0] + x_step * step != coord1[0] or coord2[1] + y_step * step != coord1[1]:
        if mapa[(coord2[0] + x_step * step, coord2[1] + y_step * step)] == '#':
            view_is_clear = False
            break
        step += 1

    return view_is_clear


# print(is_view_clear((3, 4), (1, 0), mapa))
# print(is_view_clear((0, 2), (4, 2), mapa))

def find_best_position(asteroids, mapa):
    count = [0] * len(asteroids)
    for index, asteroid1 in enumerate(asteroids):
        for asteroid2 in asteroids:
            if asteroid1 != asteroid2:
                if is_view_clear(asteroid1, asteroid2, mapa):
                    count[index] += 1
        print(f"Asteroid {asteroid1} sees {count[index]} other asteroids.")

    print(np.array(count).max())
    return np.array(count).max()


def print_map(mapa, max_x, max_y):
    for j in range(max_y):
        line = []
        for i in range(max_x):
            line.append(mapa[i, j])
        print(''.join(line))


base = (26, 29)  # 299 asteroids
asteroids.remove(base)
to_remove = []
for asteroid in asteroids:
    if not is_view_clear(base, asteroid, mapa):
        to_remove.append(asteroid)


for ast in to_remove:
    mapa[ast] = '.'
    asteroids.remove(ast)

print(len(asteroids))

uhly = [0] * 299
for j, asteroid in enumerate(asteroids):
    if asteroid[0] >= 26 and asteroid[1] < 29:
        uhly[j] = atan(abs(asteroid[0] - 26) / abs(asteroid[1] - 29))
    elif asteroid[0] > 26 and asteroid[1] == 29:
        uhly[j] = pi / 2
    elif asteroid[0] > 26 and asteroid[1] >= 29:
        uhly[j] = pi - atan(abs(asteroid[0] - 26) / abs(asteroid[1] - 29))
    elif asteroid[0] <= 26 and asteroid[1] > 29:
        uhly[j] = atan(abs(asteroid[0] - 26) / abs(asteroid[1] - 29)) + pi
    elif asteroid[0] < 26 and asteroid[1] == 29:
        uhly[j] = pi / 2 * 3
    else:
        uhly[j] = 2 * pi - atan(abs(asteroid[0] - 26) / abs(asteroid[1] - 29))

uhly_orig = uhly.copy()
uhly.sort()
v = uhly[199]
index = uhly_orig.index(v)
print(asteroids[index])


# print_map(mapa, max_x + 1, max_y + 1)


# print(asteroids)
