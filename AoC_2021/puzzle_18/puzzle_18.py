from utils.puzzle import Puzzle


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
    # data = p.load_input()
    data = p.load_input("input_test.txt")

    first = load_sn(data[0])
    second = load_sn(data[1])
    ab = first.add(second)
    print(ab.v)
    print(ab.d)

    print()
    c = load_sn(data[2])
    print(c.v)
    print(c.d)
    print()

    c.explode()
    print(c.v)
    print(c.d)

    print()
