from pathlib import Path
import re
from collections import defaultdict

filename = "input_24.txt"
data = []
with Path(filename).open() as file:
    for line in file:
        data.append(re.findall(r'(ne|se|sw|nw|e|w)', line.strip()))


def move_to(x, y, course: str):
    if course == 'e':
        return x + 1, y
    elif course == 'w':
        return x - 1, y
    elif course == 'se':
        return x + 1, y - 1
    elif course == 'sw':
        return x, y - 1
    elif course == 'ne':
        return x, y + 1
    elif course == 'nw':
        return x - 1, y + 1
    else:
        Exception("no course")


def adjacent_tiles(x, y, hall):
    return sum([hall[move_to(x, y, d)] for d in ['e', 'w', 'ne', 'nw', 'sw', 'se']])


hall = defaultdict(lambda: False)
for path in data:
    x = y = 0
    for course in path:
        x, y = move_to(x, y, course)
    hall[(x, y)] = not hall[(x, y)]

print(sum(hall.values()))

for day in range(1, 101):
    # cleaning of the hall -> minimal hall
    black_tiles_hall_with_adjacent_white = defaultdict(lambda: False)
    for tile, color in hall.items():
        if color:
            black_tiles_hall_with_adjacent_white[tile] = True
            adjacent_tiles(*tile, black_tiles_hall_with_adjacent_white)
    new_hall = defaultdict(lambda: False)
    for tile in black_tiles_hall_with_adjacent_white:
        # messing only hall dict. Keep black_tiles_hall_with_adjacent_white intact
        if hall[tile]:
            adj = adjacent_tiles(*tile, hall)
            if adj == 0 or adj > 2:
                new_hall[tile] = False
            else:
                new_hall[tile] = True
        else:
            if adjacent_tiles(*tile, hall) == 2:
                new_hall[tile] = True

    hall = new_hall
    print(f'Day {day}: {sum(hall.values())}')
