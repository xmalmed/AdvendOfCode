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

class Scan():
    def __init__(self, coordinates: list):
        self.coordinates = coordinates
        self.start_directions = self.initial_directions()


    def initial_directions(self):
        start_directionsnces = {}
        for i in range(len(self.coordinates) - 1):
            for j in range(i + 1, len(self.coordinates)):
                v = (
                        (self.coordinates[j][0] - self.coordinates[i][0]),
                        + (self.coordinates[j][1] - self.coordinates[i][1]),
                        + (self.coordinates[j][2] - self.coordinates[i][2]),
                )
                start_directionsnces[(i, j)] = v
        return start_directionsnces


if __name__ == "__main__":
    p = Puzzle()
    # data = p.load_input()
    # data = p.load_input('input_test.txt')
    data = p.load_input("input_test2.txt")

    scanners = []
    for line in data:
        if match(r"--- scanner", line):
            scanner = []
        elif line == "":
            scanners.append(Scan(scanner))
            scanner = []
        else:
            scanner.append(tuple(int(x) for x in line.split(",")))
    if scanner:
        scanners.append(Scan(scanner))


    print(scanners[0].initial_directions())
