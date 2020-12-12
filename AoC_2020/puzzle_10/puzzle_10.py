from pathlib import Path
from itertools import chain, combinations

numbers = list(map(int, Path('input_10.txt').read_text().split()))

sorted_numbers = sorted(numbers)
sorted_numbers.insert(0, 0)
sorted_numbers.append(sorted_numbers[-1] + 3)


def validate_seq(seq):
    for i in range(len(seq) - 1):
        if seq[i + 1] - seq[i] <= 3:
            return True
        else:
            return False


dist = [0, 0, 0, 0]  # 0, 1, 2, 3
seqs = [[]]
for i in range(len(sorted_numbers) - 1):
    dist[sorted_numbers[i + 1] - sorted_numbers[i]] += 1
    if sorted_numbers[i + 1] - sorted_numbers[i] == 1:
        seqs[-1].append((sorted_numbers[i + 1]))
    else:
        if seqs[-1] != []:
            seqs.append([])
        print("************************")

print(dist)
print(dist[1] * dist[3])

total = 1
for seq in seqs:
    zeq = seq[:-1]
    count = 0
    if zeq != []:
        powerset = chain.from_iterable(combinations(range(len(zeq)), r) for r in range(len(zeq)+1))
        for com in powerset:
            try_seq = [zeq[item] for item in com]
            valid = validate_seq([zeq[0] - 1] + try_seq + [zeq[-1] + 1])
            if valid:
                count += 1
        print(zeq)
        print(count)
        total *= count

print(total)




# intervals = []
# for seq in range(1, len(sorted_numbers) - 1):
#     print()
