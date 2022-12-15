from utils.puzzle import Puzzle
from parse import parse
from timeit import default_timer

LIMIT = 4_000_000 + 1


# LIMIT = 20 + 1


def manhatan_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def unite_ranges(ranges):
    ranges.sort(key=lambda x: x[1] - x[0])
    x, y = ranges.pop()
    count = 0
    while ranges:
        if x <= 0 and y >= LIMIT - 1:
            return False
        count += 1
        r = ranges.pop()
        if r[0] < LIMIT and max(r[0], 0) < x and x <= r[1] <= y:
            x = r[0]
        elif r[1] >= 0 and r[1] > y >= r[0] >= x:
            y = r[1]
        else:
            ranges.insert(0, r)
        if count == 100:
            return (x, y), ranges

    return not (x <= 0 and y >= LIMIT - 1)


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    start = default_timer()
    for i, sensor in enumerate(data):
        sx, sy, bx, by = parse('Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}', sensor)
        data[i] = (sx, sy, bx, by, manhatan_dist(sx, sy, bx, by))

    scans = set()
    for Y in range(0, LIMIT).__reversed__():
        if Y % 100_000 == 0:
            print(Y)
        ranges = []
        for sensor in data:
            dist = sensor[4]
            diff = abs(Y - sensor[1])
            if Y == 2_000_000:
                scans = scans.union(set(range(sensor[0] - (dist - diff), sensor[0] + 1 + (dist - diff))))
            x = max(sensor[0] - (dist - diff), 0)
            y = min(sensor[0] + 1 + (dist - diff), LIMIT)
            ranges.append((x, y))

        if res := unite_ranges(ranges):
            print(f"Part 2: Frequency =  {4_000_000 * res[0][1] + Y}, (X = {res[0][1]}, Y = {Y})")
            break
        if Y == 2_000_000:
            print(f"Part 1: {len(scans)} - 1 for a beacon.")

    end = default_timer()
    print(end - start)
