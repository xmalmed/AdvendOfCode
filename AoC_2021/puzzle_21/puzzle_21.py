from utils.puzzle import Puzzle
from parse import parse


def count_turn(games):
    wins, cont = 0, 0
    next_games = []
    for (p, s, n) in games:
        for k, v in DICE3.items():
            np = (p + k - 1) % 10 + 1
            ns = s + np
            nn = n * v
            if ns >= 21:
                wins += nn
            else:
                cont += nn
                next_games.append((np, ns, nn))
    return wins, cont, next_games


def count_games_of_player(start_position):
    games = [(start_position, 0, 1)]
    spaces = []
    while games:
        wins, cont, games = count_turn(games)
        spaces.append((wins, cont))
    return spaces


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

    # part 2
    DICE3 = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    spaces1 = count_games_of_player(p1)
    spaces2 = count_games_of_player(p2)

    p1_wins = 0
    for i, w in enumerate(spaces1):
        if i == 0:
            continue
        p1_wins += w[0] * spaces2[i - 1][1]

    p2_wins = 0
    for i, w in enumerate(spaces2):
        p2_wins += w[0] * spaces1[i][1]

    print(p1_wins)
    print(p2_wins)
