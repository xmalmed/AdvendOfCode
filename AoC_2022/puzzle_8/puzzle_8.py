from utils.puzzle import Puzzle


def find_visible(main, second, is_x=True):
    for i in main:
        if is_x:
            x = i
        else:
            y = i
        max_tree = -1
        for j in second:
            if is_x:
                y = j
            else:
                x = j
            if forest[y][x] > max_tree:
                visible[y][x] = 1
                max_tree = forest[y][x]
                if max_tree >= 9:
                    break


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input(string=True)
    # data = p.load_input("input_test.txt", string=True)

    forest = []
    size = len(data)
    visible = [[1] + [0]*(size-2) + [1] for _ in range(size-2)]
    visible.append([1]*size)
    visible.insert(0, [1]*size)
    for line in data:
        forest.append([int(x) for x in list(line)])

    find_visible(range(size), range(size))
    find_visible(range(size), range(size - 1, -1, -1))
    find_visible(range(size), range(size), is_x=False)
    find_visible(range(size), range(size - 1, -1, -1), is_x=False)
    print(f"Total visible trees: {sum([sum(l) for l in visible])}")

    max_score = 0
    for tx in range(1, size-1):
        for ty in range(1, size-1):
            score = 1
            h = forest[ty][tx]
            trees = 0
            for x in range(tx + 1, size):
                trees += 1
                if forest[ty][x] >= h:
                    break
            score *= trees
            trees = 0
            for x in range(tx - 1, -1, -1):
                trees += 1
                if forest[ty][x] >= h:
                    break
            score *= trees
            trees = 0
            for y in range(ty + 1, size):
                trees += 1
                if forest[y][tx] >= h:
                    break
            score *= trees
            trees = 0
            for y in range(ty - 1, -1, -1):
                trees += 1
                if forest[y][tx] >= h:
                    break
            score *= trees
            if max_score < score:
                max_score = score

    print(f"Max scenic score: {max_score}")
