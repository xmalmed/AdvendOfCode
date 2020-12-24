from pathlib import Path
import numpy as np
from collections import defaultdict
from itertools import product

filename = "input_17.txt"
# filename = "input_17_test.txt"
data = dict()
with Path(filename).open() as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            if char == "#":
                data[(x, -y)] = True


def adjacent_cubes(coord, space):
    all_directions = set(product(*[[-1, 0, 1]] * len(coord))) - {(0,) * len(coord)}
    adjacent_cube_coords = [np.array(d) + np.array(coord) for d in all_directions]
    return sum([space[tuple(coord)] for coord in adjacent_cube_coords])


def fill_start_space(dim, data, space):
    for coord2d, state in data.items():
        new_c = (*coord2d, *((0, ) * (dim - 2)))
        space[new_c] = state


dim = 4
space = defaultdict(lambda: False)
fill_start_space(dim, data, space)

for cycle in range(1, 7):
    # cleaning of the hall -> minimal hall
    active_cubes_with_adjacent = defaultdict(lambda: False)
    for cube, state in space.items():
        if state:
            active_cubes_with_adjacent[cube] = True
            adjacent_cubes(cube, active_cubes_with_adjacent)
    new_space = defaultdict(lambda: False)
    for cube in active_cubes_with_adjacent:
        # messing only space dict. Keep active_cubes_with_adjacent intact
        if space[cube]:
            adj = adjacent_cubes(cube, space)
            if adj == 2 or adj == 3:
                new_space[cube] = True
            else:
                new_space[cube] = False
        else:
            if adjacent_cubes(cube, space) == 3:
                new_space[cube] = True

    space = new_space
    print(f'Cycle {cycle}: {sum(space.values())}')
