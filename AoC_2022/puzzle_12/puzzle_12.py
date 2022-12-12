from utils.puzzle import Puzzle
from math import inf
import numpy as np


def update_path(pos, n):
    if path[pos[1]][pos[0]] > n:
        path[pos[1]][pos[0]] = n
        return True
    else:
        return False


def next_moves(pos, x_max, y_max, n):
    new_steps = []
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new = tuple(np.add(d, pos))
        if (
            (0 <= new[0] < x_max)
            and (0 <= new[1] < y_max)
            and (maze[new[1]][new[0]] - maze[pos[1]][pos[0]] <= 1)
        ):
            if update_path(new, n + 1):
                new_steps.append(new)
                if new == end:
                    new_steps = False
                    break
    return new_steps


def run(steps, path):
    n = 0
    for s in steps:
        path[s[1]][s[0]] = n
    searching = True
    while searching:
        new_steps = []
        while steps:
            pos = steps.pop()
            ns = next_moves(pos, x_max, y_max, n)
            if ns is False:
                searching = False
                break
            new_steps += ns

        steps = new_steps
        n += 1
    print(f"Number of steps: {n}")


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")
    x_max = len(data[0])
    y_max = len(data)
    maze = []
    path = [[inf] * x_max for _ in range(y_max)]
    new_starts = []

    for y, d in enumerate(data):
        line = []
        for x, ch in enumerate(d):
            if ch == "a":
                new_starts.append((x, y))
            if ch == "S":
                start = (x, y)
                ch = "a"
            if ch == "E":
                end = (x, y)
                ch = "z"
            line.append(ord(ch) - 97)
        maze.append(line)

    print("part 1")
    run([start], path)
    print("part 2, reusing previous path")
    run(new_starts, path)
