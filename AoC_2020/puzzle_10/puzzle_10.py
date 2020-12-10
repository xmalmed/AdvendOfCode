from pathlib import Path

numbers = list(map(int, Path('input_10.txt').read_text().split()))

sorted_numbers = sorted(numbers)
sorted_numbers.insert(0, 0)
sorted_numbers.append(sorted_numbers[-1] + 3)

dist = [0, 0, 0, 0]  # 0, 1, 2, 3
for i in range(len(sorted_numbers) - 1):
    dist[sorted_numbers[i + 1] - sorted_numbers[i]] += 1

print(dist)
print(dist[1] * dist[3])


for 
