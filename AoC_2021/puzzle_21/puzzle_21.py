from utils.puzzle import Puzzle
from parse import parse

if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")
    (p1,) = parse("Player 1 starting position: {:d}", data[0])
    (p2,) = parse("Player 2 starting position: {:d}", data[1])
    players = [p1, p2]
    scores = [0, 0]
    dice = 1
    winner = False
    throws = 0
    whose_turn = 0
    while not winner:
        dice_sum = 0
        for _ in range(3):
            throws += 1
            dice_sum += dice
            dice += 1
            dice = ((dice - 1) % 100) + 1
        players[whose_turn] = ((players[whose_turn] + dice_sum - 1) % 10) + 1
        scores[whose_turn] += players[whose_turn]
        if scores[whose_turn] >= 1000:
            print(whose_turn, throws, scores)
            print(throws * min(scores))
            winner = True
        whose_turn = (whose_turn + 1) % len(players)

