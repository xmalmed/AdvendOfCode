from utils.puzzle import Puzzle
from parse import parse


class Cave:
    def __init__(self, name):
        # if name.isupper():
        self.name = name
        self.neighbours = []

    # def neighbours(self):
    #     pass
    #
    # def add_neighbour(self, n):


if __name__ == '__main__':
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    caves = {}
    for line in data:
        a, b = parse('{}-{}', line)
        if not a in caves:
            caves[a] = Cave(a)
        if not b in caves:
            caves[b] = Cave(b)
        caves[a].neighbours.append(caves[b])
        caves[b].neighbours.append(caves[a])

    # for c in caves.values():
    #     print(c.name, [n.name for n in c.neighbours])

    paths = [['start']]
    end_paths = set()
    while len(paths) > 0:
        path = paths.pop(0)
        for n in caves[path[-1]].neighbours:
            if n.name == 'end':
                end_paths.add('-'.join(path + [n.name]))
            elif (n.name.islower() and n.name not in path) or n.name.isupper():
                paths.append(path + [n.name])

    for e in end_paths:
        print(e)
    print(len(end_paths))
