from pathlib import Path
from puzzle_1.puzzle_1 import find_sum_of_two
from time import time

start_time = time()

# numbers = list(map(int, Path('input_test_9.txt').read_text().split()))
numbers = list(map(int, Path('input_9.txt').read_text().split()))

# span = 5
span = 25
counter = -1
trying = True

# part 1
while trying:
    counter += 1
    trying = find_sum_of_two(numbers[counter:span + counter], numbers[span + counter])

print(numbers[span + counter])  # 1721308972
target = numbers[span + counter]

# part 2
start = -1
lenght = 0
encrypting = True
total = 0 # numbers[0]
while encrypting:
    start += 1
    while total < target:
        lenght += 1
        total += numbers[start + lenght - 1]
    if total == target:
        ma = max(numbers[start:start + lenght - 1])
        mi = min(numbers[start:start + lenght - 1])
        # print(f'Found {numbers[start]} and {numbers[start + lenght - 1]} = {numbers[start] + numbers[start + lenght - 1]}')
        print(f'Found {mi} and {ma} = {mi + ma}')
        encrypting = False  # mean done
    else:
        total = total - numbers[start] - numbers[start + lenght - 1]
        lenght -= 2

end = time()
print(end - start_time)
