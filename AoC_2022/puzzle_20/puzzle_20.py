from utils.puzzle import Puzzle

KEY = 811589153


class CircleItem:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.nex = None

#
# class CircleList:
#     def __init__(self, l: list):
#         self.items = {}
#         first = CircleItem(l[0])
#         for v in l[1:]:
#             new = CircleItem(v)
#             self.items[new] = True



if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")
    l = len(data)

    nums = []
    first = CircleItem(data[0])
    nums.append(first)
    for v in data[1:]:
        new = CircleItem(v)
        if v == 0:
            zero = new
        new.prev = nums[-1]
        nums[-1].nex = new
        nums.append(new)
    nums[0].prev = nums[-1]
    nums[-1].nex = nums[0]

    for i in range(len(data)):
        current = nums[i]
        neg = current.value < 0
        moves = 1 if neg else 0
        moves = moves + (abs(current.value) % (l-1) )
        if moves == 0:
            continue
        n = current
        for _ in range(abs(moves)):
            if neg:
                n = n.prev
                if n == current:
                    n = n.prev
            else:
                n = n.nex
                if n == current:
                    n = n.nex
        current.prev.nex = current.nex
        current.nex.prev = current.prev
        n.nex.prev = current
        current.nex = n.nex
        n.nex = current
        current.prev = n

    n = zero
    results = []
    for i in range(1,3001):
        n = n.nex
        if i % 1000 == 0:
            results.append(n.value)
    print(results, sum(results))


    # 10831 part 1

    nums = []
    first = CircleItem(data[0]*KEY)
    nums.append(first)
    for v in data[1:]:
        new = CircleItem(v*KEY)
        if v == 0:
            zero = new
        new.prev = nums[-1]
        nums[-1].nex = new
        nums.append(new)
    nums[0].prev = nums[-1]
    nums[-1].nex = nums[0]

    for _ in range(10):
        for i in range(len(data)):
            current = nums[i]
            neg = current.value < 0
            moves = 1 if neg else 0
            moves = moves + (abs(current.value) % (l - 1))
            if moves == 0:
                continue
            n = current
            for _ in range(abs(moves)):
                if neg:
                    n = n.prev
                    if n == current:
                        n = n.prev
                else:
                    n = n.nex
                    if n == current:
                        n = n.nex
            current.prev.nex = current.nex
            current.nex.prev = current.prev
            n.nex.prev = current
            current.nex = n.nex
            n.nex = current
            current.prev = n

    n = zero
    results = []
    for i in range(1, 3001):
        n = n.nex
        if i % 1000 == 0:
            results.append(n.value)
    print(results, sum(results))