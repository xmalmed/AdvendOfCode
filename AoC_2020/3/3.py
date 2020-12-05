import math


def load_input():
    file_lines = []
    with open("input_3.txt", 'r') as lines:
        for line in lines:
            file_lines.append(line.strip('\n'))
    return file_lines


def count_trees(maze, x_step=3, y_step=1):
    trees = 0
    x = 0
    x_size = len(maze[0])

    for (i, line) in enumerate(maze):
        if i % y_step:
            # print(f'Skip line {i}')
            continue
        if line[x] == '#':
            trees += 1
        x = (x + x_step) % x_size
    return trees


maze = load_input()

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees_on_slopes = []
for (x, y) in slopes:
    trees_on_slopes.append(count_trees(maze, x, y))

print(trees_on_slopes)
print(math.prod(trees_on_slopes))
