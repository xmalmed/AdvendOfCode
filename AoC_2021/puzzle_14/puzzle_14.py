from utils.puzzle import Puzzle
from parse import parse
from collections import defaultdict


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    template = data.pop(0) + "ř"
    data.pop(0)
    pairs = {}
    for line in data:
        find, insert = parse("{} -> {}", line)
        pairs[find] = insert

    polymer = defaultdict(lambda: 0)
    for i in range(1, len(template)):
        polymer[template[i - 1 : i + 1]] += 1

    # part 1
    # for step in range(10):
    # part 2
    for step in range(40):
        print(step)
        new_polymer = defaultdict(lambda: 0)
        for pair in polymer:
            if pair in pairs:
                new_polymer[pair[0] + pairs[pair]] += polymer[pair]
                new_polymer[pairs[pair] + pair[1]] += polymer[pair]
            else:
                new_polymer[pair] += polymer[pair]
        polymer = new_polymer

    letters = defaultdict(lambda: 0)
    for pair in polymer:
        letters[pair[0]] += polymer[pair]
    results = list(letters.items())
    results.sort(key=lambda x: x[1])
    print(letters)
    print(results[-1][1] - results[0][1])

    # old part 1
    # for _ in range(10):
    #     length = len(template)
    #     i = 1
    #     while i <= length:
    #         if (pair := template[i-1:i+1]) in pairs:
    #             template = template[:i] + pairs[pair] + template[i:]
    #             length += 1
    #             i += 2
    #         else:
    #             i += 1
    #
    # letters = defaultdict(lambda: 0)
    # for ch in template:
    #     letters[ch] += 1
    # results = list(letters.items())
    # results.sort(key=lambda x: x[1])
    # print(letters)
    # print(results[-1][1]-results[0][1])
