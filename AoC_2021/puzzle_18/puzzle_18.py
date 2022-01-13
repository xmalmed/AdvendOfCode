from utils.puzzle import Puzzle
from math import floor, ceil


class Sn:

    POWER = 5
    SN = 2 ** POWER

    def __init__(self):
        self.d = [-1] * Sn.SN
        self.v = [-1] * Sn.SN

    def add(self, b):
        c = Sn()
        for i, d in enumerate(self.d):
            if d != -1:
                c.d[i // 2] = d + 1
                c.v[i // 2] = self.v[i]
        for j, d in enumerate(b.d):
            if d != -1:
                c.d[j // 2 + Sn.SN // 2] = d + 1
                c.v[j // 2 + Sn.SN // 2] = b.v[j]
        return c

    def explode(self):
        for i, d in enumerate(self.d):
            if d == Sn.POWER:
                v1 = self.v[i]
                v2 = self.v[i + 1]
                self.v[i] = 0
                self.v[i + 1] = -1
                self.d[i] += -1
                self.d[i + 1] = -1
                for j in range(i).__reversed__():
                    if self.d[j] != -1:
                        self.v[j] += v1
                        break
                for k in range(i + 2, Sn.SN):
                    if self.d[k] != -1:
                        self.v[k] += v2
                        break

    def split(self):
        for i, v in enumerate(self.v):
            if v > 9:
                d = self.d[i]
                self.v[i] = floor(v / 2)
                self.d[i] = d + 1
                j = i + Sn.SN // 2 ** (d + 1)
                self.v[j] = ceil(v / 2)
                self.d[j] = d + 1
                return True
        return False

    def reduce(self):
        splited = True
        while splited:
            self.explode()
            splited = self.split()

    def magnitude(self):
        m = self.v.copy()
        dd = self.d.copy()
        for depth in range(1, Sn.POWER).__reversed__():
            for i in range(self.SN):
                if dd[i] == depth:
                    j = i + Sn.SN // 2 ** depth
                    m[i] = 3 * m[i] + 2 * m[j]
                    dd[i] += -1
                    dd[j] = -1
                    m[j] = -1

        return m[0]


def load_sn(text):
    sn_list = eval(text)
    sn = Sn()

    def find_leaf(sn_list, path):
        for j in range(2):
            if isinstance(sn_list[j], int):
                depth = len(path) + 1
                new_path = path + str(j)
                while len(new_path) < Sn.POWER:
                    new_path += "0"
                index = int(new_path, 2)
                sn.d[index] = depth
                sn.v[index] = sn_list[j]
            else:
                find_leaf(sn_list[j], path + str(j))

    find_leaf(sn_list, "")
    return sn


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    last = load_sn(data[0])
    sn_list = [last]
    for line in data[1:]:
        sn = load_sn(line)
        sn_list.append(sn)
        new = last.add(sn)
        new.reduce()
        last = new

    print("Snailfish homework magnitude is: ", last.magnitude())

    sn_max = -1
    for i in range(len(sn_list)):
        for j in range(len(sn_list)):
            sn = sn_list[i].add(sn_list[j])
            sn.reduce()
            m = sn.magnitude()
            if m > sn_max:
                sn_max = m
    print("Snailfish max magnitude is: ", sn_max)
