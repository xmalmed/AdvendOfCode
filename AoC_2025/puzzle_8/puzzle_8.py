from utils.puzzle import Puzzle


def distance(data1, data2):
    x1, y1, z1 = data1
    x2, y2, z2 = data2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2


if __name__ == '__main__':
    p = Puzzle(day=8, year=2025)
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    boxes = []
    for line in data:
        (x, y, z) = map(int, line.split(','))
        boxes.append((x, y, z))

    distances = {}
    n = len(boxes)
    for i, box in enumerate(boxes):
        for j in range(i + 1, n):
            d = distance(box, boxes[j])
            assert d not in distances
            distances[d] = (box, boxes[j])

    dists_list = list(distances.keys())
    dists_list.sort()

    circuits = []
    counter = 0
    while len(circuits) != 1 or len(circuits[0]) != len(boxes):
        i = counter
        counter += 1
        d = dists_list[i]
        b1, b2 = distances[d]
        # print(f"Distance: {d} between boxes {b1} and {b2}")

        c1 = None
        c2 = None
        same = False
        for c in circuits:
            if b1 in c and b2 in c:
                same = True
                break
            elif b1 in c:
                c1 = c
            elif b2 in c:
                c2 = c

        if c1 and c2:
            c1.extend(c2)
            circuits.remove(c2)
        elif c1:
            c1.append(b2)
        elif c2:
            c2.append(b1)
        elif not same:
            circuits.append([b1, b2])
        # print(circuits)

    # sizes = [len(c) for c in circuits]
    # sizes.sort(reverse=True)
    # print(sizes[0] * sizes[1] * sizes[2])
    print(b1, b2)
    print(b1[0] * b2[0])
