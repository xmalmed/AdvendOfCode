from utils.puzzle import Puzzle
from re import match
import numpy as np

RZ = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
RY = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
RX = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
FLIP = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])





# def align(scan1, scan2):
#     d1 = get_distances(scan1)
#     d2 = get_distances(scan2)
#     for d in d1:
#         i = None
#         try:
#             i = [dd[2] for dd in d2].index(d)
#         except ValueError:
#             pass
#         if i:
#             break
#     # s1 d
#     # d2[i]

class Map:

    def __init__(self):
        self.beacons = None
        self.distance_list = None
        self.distance_set = None

    def is_overlapped(self, scan):
        overlap = self.distance_set.intersection(scan.distance_set)
        return overlap

    def calculate_distance_list(self):
        d_list = []
        for i in range(len(self.beacons) - 1):
            for j in range(i + 1, len(self.beacons)):
                d = np.dot((self.beacons[i] - self.beacons[j]), (self.beacons[i] - self.beacons[j]))
                d_list.append([d, self.beacons[i], self.beacons[j]])
        return d_list

    def get_distance_set(self):
        return set(d[0] for d in self.distance_list)

    def merge_scan(self, scan):
        if self.beacons is None:
            self.beacons = scan.beacons.copy()
            self.distance_list = scan.distance_list.copy()
            self.distance_set = scan.distance_set.copy()
        else:
            self.beacons = np.unique(np.vstack([self.beacons, scan.beacons]), axis=0)
            self.distance_list = self.calculate_distance_list()
            self.distance_set = self.get_distance_set()


class Scanner(Map):

    def __init__(self, beacons: list, name):
        super().__init__()
        self.name = name
        self.beacons = beacons
        self.distance_list = self.calculate_distance_list()
        self.distance_set = self.get_distance_set()
        self.rot = self.rotations()

    def rotateZ(self):
        self.beacons = [RZ @ b for b in self.beacons]

    def rotateY(self):
        self.beacons = [RY @ b for b in self.beacons]

    def rotateX(self):
        self.beacons = [RX @ b for b in self.beacons]

    def flip(self):
        self.beacons = [FLIP @ b for b in self.beacons]

    def shift(self, v):
        self.beacons = [b + v for b in self.beacons]

    def align(self, m, d):
        bs1, bs2 = next((b[1], b[2]) for b in self.distance_list if b[0] == d)
        bm1, bm2 = next((b[1], b[2]) for b in m.distance_list if b[0] == d)
        shiftA = bm1 - bs1
        shiftB = bm1 - bs2

        if (bs2 + shiftA == bm2).all():
            # print(shiftA)
            return shiftA

        elif (bs1 + shiftB == bm2).all():
            # print(shiftB)
            return shiftB
        else:
            # print('no match')
            return None
            # TODO: I might want to check more beacons, not only the first.

    def rotations(self):
        for i in range(3):
            for _ in range(4):
                self.rotateZ()
                yield self
            self.rotateX()
            self.rotateX()
            for _ in range(4):
                self.rotateZ()
                yield self
            if i == 0:
                self.rotateX()
            elif i == 1:
                self.rotateY()




if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input('input_test.txt')
    # data = p.load_input("input_test2.txt")

    scanners = []
    for line in data:
        if match(r"--- scanner", line):
            name = line
            scanner = []
        elif line == "":
            scanners.append(Scanner(scanner, name))
            scanner = []
        else:
            scanner.append(np.array([int(x) for x in line.split(",")]))
    if scanner:
        scanners.append(Scanner(scanner, name))

    m = Map()
    m.merge_scan(scanners.pop(0))


    ss = [np.array((0,0,0))]

    while scanners:
        s = scanners.pop(0)
        print('trying: ' + s.name)
        distances = m.is_overlapped(s)
        if len(distances) >= (12**2-12)/2:
            d1 = distances.pop()
            d2 = distances.pop()
            for ii in range(24):
                next(s.rot)
                s.distance_list = s.calculate_distance_list()
                if (a1 := s.align(m, d1)) is not None and (a2 := s.align(m, d2)) is not None:
                    if (a1 == a2).all() or (a1 == -1 * a2).all():
                        s.shift(a1)
                        m.merge_scan(s)
                        ss.append(a1)
                        # print(s.name)
                        break
        else:
            scanners.append(s)


    print(len(m.beacons))

    max = 0
    for s1 in ss:
        for s2 in ss:
            dd = sum(abs(s1 - s2))
            if dd > max:
                max = dd

    print(max)