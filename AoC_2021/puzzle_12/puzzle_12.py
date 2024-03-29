from utils.puzzle import Puzzle
from parse import parse


class Cave:
    def __init__(self, name):
        self.name = name
        self.neighbours = []


def find_all_paths(start_path, repeat=None):
    paths = start_path
    end_paths = set()
    while len(paths) > 0:
        path = paths.pop(0)
        for n in caves[path[-1]].neighbours:
            if n.name == "end":
                end_paths.add("-".join(path + [n.name]))
            elif n.name == "start":
                continue
            elif (n.name.islower() and n.name not in path) or n.name.isupper():
                paths.append(path + [n.name])
            elif repeat is not None:
                repeat.append(path + [n.name])
    return end_paths


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    caves = {}
    for line in data:
        a, b = parse("{}-{}", line)
        if not a in caves:
            caves[a] = Cave(a)
        if not b in caves:
            caves[b] = Cave(b)
        caves[a].neighbours.append(caves[b])
        caves[b].neighbours.append(caves[a])

    repeat_paths = []
    end_paths1 = find_all_paths([["start"]], repeat_paths)
    print(len(end_paths1))

    end_paths2 = find_all_paths(repeat_paths)
    print(len(end_paths2) + len(end_paths1))
