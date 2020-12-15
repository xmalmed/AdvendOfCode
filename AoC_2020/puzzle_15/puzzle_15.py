from collections import defaultdict

# START = [0, 3, 6] # test
# END = 10  # test
START = [8, 13, 1, 0, 18, 9]
END = 30000000

numbers = defaultdict(list)

for i in range(len(START)):
    numbers[START[i]].append(i + 1)

last = START[-1]
for i in range(len(START) + 1, END + 1):
    if len(numbers[last]) == 1 and numbers[last][-1] == i - 1:
        last = 0
        numbers[last].append(i)
    else:
        last = numbers[last][-1] - numbers[last][-2]
        numbers[last].append(i)
    if i == 2020:
        print(f'kolo {i}: {last};')


# print(f'kolo {i}: {last}; {numbers}')
print(f'kolo {i}: {last};')
