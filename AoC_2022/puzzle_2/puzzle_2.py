from utils.puzzle import Puzzle


GAME = {
    "X": ["A Z", "B X", "C Y"],
    "Y": ["A X", "B Y", "C Z"],
    "Z": ["A Y", "B Z", "C X"],
}


def compare(round: str) -> int:
    if round in GAME["X"]:
        return 0
    if round in GAME["Y"]:
        return 3
    if round in GAME["Z"]:
        return 6


def value(round: str) -> int:
    return {"X": 1, "Y": 2, "Z": 3}[round[2]]


def score2(round: str) -> str:
    variant = GAME[round[2]]
    transformed_round = next(t for t in variant if t.startswith(round[0]))
    return compare(transformed_round) + value(transformed_round)


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    total_score = total_score_2 = 0
    for round in data:
        total_score += compare(round) + value(round)
        total_score_2 += score2(round)

    print(f"Part 1 score: {total_score}")
    print(f"Part 2 score: {total_score_2}")
