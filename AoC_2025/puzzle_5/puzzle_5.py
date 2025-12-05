from utils.puzzle import Puzzle

if __name__ == '__main__':
    p = Puzzle(day=5, year=2025)
    data = p.load_input()
    # data = p.load_input('input_test.txt')

line = data.pop(0)
id_ranges = []
while line != '':
    a, b = line.split('-')
    id_ranges.append((int(a), int(b)))
    line = data.pop(0)

count = 0
for id in data:
    id = int(id)
    for a, b in id_ranges:
        if a <= id <= b:
            # print(f'ID {id} is blocked by range {a}-{b}')
            count += 1
            break

print(count)

total = 0
id_ranges.sort()
range = id_ranges[0]
for a, b in id_ranges:
    if a <= range[1]:
        range = (range[0], max(range[1], b))
    else:
        total += range[1] - range[0] + 1
        range = (a, b)

total += range[1] - range[0] + 1
print(total)

