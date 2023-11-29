from utils.puzzle import Puzzle
from re import match
import numpy as np

RZ = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
RY = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
RX = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])





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


class Scanner:

    def __init__(self, beacons: list):
        self.beacons = beacons
        self.distance_net = self.calculate_net_distances()
        self.distance_set = set(self.distance_net.values())

    def calculate_net_distances(self):
        distances = {}
        for i in range(len(self.beacons) - 1):
            for j in range(i + 1, len(self.beacons)):
                d = np.dot((self.beacons[i] - self.beacons[j]), (self.beacons[i] - self.beacons[j]))
                distances[(i, j)] = d
        return distances

    def rotateZ(self):
        self.beacons = [RZ @ b for b in self.beacons]

    def rotateY(self):
        self.beacons = [RY @ b for b in self.beacons]

    def rotateX(self):
        self.beacons = [RX @ b for b in self.beacons]

    def is_overlapped(self, scan2):
        overlap = self.distance_set.intersection(scan2.distance_set)
        return overlap

    def overlap(self, scan2, distances):
        d = distances.pop()
        key1 = next(key for key in self.distance_net if self.distance_net[key] == d)
        key2 = next(key for key in scan2.distance_net if scan2.distance_net[key] == d)
        beacon2 = scan2.beacons[key2[0]]
        shiftA = beacon2 - self.beacons[key1[0]]
        shiftB = beacon2 - self.beacons[key1[1]]

        testA = [b + shiftA for b in self.beacons]

        ###



        testB = [b + shiftB for b in self.beacons]
        xxx = [key for key in scan2.distance_net if scan2.distance_net[key] in distances]
        xx = []
        for k in xxx:
            xx.append(k[0])
            xx.append(k[1])
        x = set(xx)
        for i in x:
            assert any((scan2.beacons[i] == x).all() for x in testB)


        print()





    # def initial_directions(self):
    #     start_directionsnces = {}
    #     for i in range(len(self.coordinates) - 1):
    #         for j in range(i + 1, len(self.coordinates)):
    #             v = (
    #                     (self.coordinates[j][0] - self.coordinates[i][0]),
    #                     + (self.coordinates[j][1] - self.coordinates[i][1]),
    #                     + (self.coordinates[j][2] - self.coordinates[i][2]),
    #             )
    #             start_directionsnces[(i, j)] = v
    #     return start_directionsnces





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
            scanners.append(Scanner(scanner))
            scanner = []
        else:
            scanner.append(np.array([int(x) for x in line.split(",")]))
    if scanner:
        scanners.append(Scanner(scanner))


    distances = scanners[0].is_overlapped(scanners[1])
    scanners[0].overlap(scanners[1], distances)

    print()