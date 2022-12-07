from utils.puzzle import Puzzle
# from treelib import Node, Tree

class Dir:
    def __init__(self, name, up):
        self.name = name
        self.up = up
        self.ls = {}
        self.size = 0


class File:
    def __init__(self, name, size, dir):
        self.name = name
        self.size = size
        self.dir = dir


def go_sum(root, list_dir):
    total = 0
    list_dir.append(root.size)
    for d in root.ls.values():
        if isinstance(d, Dir):
            if d.size <= 100_000:
                total += d.size
            total += go_sum(d, list_dir)
    return total


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    list_dir = []
    root = Dir('/', None)
    cwd = root
    for line in data:
        if line == "$ cd /":
            cwd = root
        elif line == '$ cd ..':
            cwd = cwd.up
        elif line == '$ ls':
            pass
        elif line.startswith('$ cd '):
            dir_name = line[5:]
            cwd = cwd.ls[dir_name]
        elif line[0] != '$':
            if line.startswith('dir '):
                cwd.ls[line[4:]] = Dir(line[4:], cwd)
            else:
                size, name = line.split(' ')
                size = int(size)
                cwd.ls[name] = File(name, size, cwd)
                up = cwd
                while up:
                    up.size += size
                    up = up.up

        else:
            print('WTF')

    print(f"part 1: {go_sum(root, list_dir)}")
    list_dir.sort()
    limit = root.size - 40_000_000
    print(f"part 2: {next(x for x in list_dir if x >= limit)}")
