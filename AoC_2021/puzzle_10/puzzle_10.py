from utils.puzzle import Puzzle

PAIRS = {")": "(", "]": "[", "}": "{", ">": "<"}
PAIRS2 = {PAIRS[k]: k for k in PAIRS}
open_brackets = PAIRS.values()

VALUES = {")": 3, "]": 57, "}": 1197, ">": 25137}
VALUES2 = {"(": 1, "[": 2, "{": 3, "<": 4}


def validate_line(line):
    lifo = []
    for bracket in line:
        if (len(lifo) == 0) or (bracket in open_brackets):
            lifo.append(bracket)
        else:
            if PAIRS[bracket] == lifo[-1]:
                lifo.pop(-1)
            else:
                return VALUES[bracket]

    return lifo


def autocomplete(lifo):
    autocomplete_scores = 0
    while lifo:
        autocomplete_scores *= 5
        autocomplete_scores += VALUES2[lifo.pop()]
    return autocomplete_scores


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    total_error = 0
    autocomplete_scores = []
    for line in data:
        res = validate_line(line)
        if isinstance(res, int):
            total_error += res
        else:
            autocomplete_scores.append(autocomplete(res))

    print("Total syntax error: ", total_error)

    autocomplete_scores.sort()
    print(
        "Autocomplete score: ", autocomplete_scores[int((len(autocomplete_scores) - 1) / 2)]
    )
