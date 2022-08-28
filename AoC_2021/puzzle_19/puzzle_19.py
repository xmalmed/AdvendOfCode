from utils.puzzle import Puzzle
from re import match


def get_distances(scan):
    distances = []
    for i in range(len(scan) - 1):
        for j in range(i + 1, len(scan)):
            d = (
                (scan[i][0] - scan[j][0]) ** 2
                + (scan[i][1] - scan[j][1]) ** 2
                + (scan[i][2] - scan[j][2]) ** 2
            )
            distances.append((i, j, d))
    return distances


def is_overlaped(scan1, scan2):
    d1 = set(d[2] for d in get_distances(scan1))
    d2 = set(d[2] for d in get_distances(scan2))
    overlap = d1.intersection(d2)
    return True if len(overlap) >= (12*11/2) else False


def align(scan1, scan2):
    d1 = get_distances(scan1)
    d2 = get_distances(scan2)
    for d in d1:
        i = None
        try:
            i = [dd[2] for dd in d2].index(d)
        except ValueError:
            pass
        if i:
            break
    # s1 d
    # d2[i]

if __name__ == "__main__":
    p = Puzzle()
    # data = p.load_input()
    data = p.load_input('input_test.txt')
    # data = p.load_input("input_test2.txt")
    scans = {}
    scan = 0
    scans[scan] = []
    for line in data:
        if match(r"--- scanner", line):
            continue
        elif line == "":
            scan += 1
            scans[scan] = []
        else:
            scans[scan].append(tuple(int(x) for x in line.split(",")))

    # distances = {}
    for i, s in scans.items():
        print(is_overlaped(scans[0], s))
        # distances[i] = get_distances(s)
