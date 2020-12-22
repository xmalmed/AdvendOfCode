from pathlib import Path

filename = "input_22.txt"
# filename = "input_22_test.txt"
deck1 = []
deck2 = []
with Path(filename).open() as file:
    while line := file.readline().strip():
        if line != "Player 1:":
            deck1.append(int(line))
    while line := file.readline().strip():
        if line != "Player 2:":
            deck2.append(int(line))


def play_game(deck1, deck2, recursion=False):
    history = [(tuple(deck1), tuple(deck2))]
    while deck1 and deck2:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if recursion and card1 <= len(deck1) and card2 <= len(deck2):
            print(">>> enter sub-game")
            sub_deck1, sub_deck2 = play_game(deck1[:card1], deck2[:card2], recursion=recursion)
            print("<<<")
            if sub_deck1:
                deck1 += [card1, card2]
            else:
                deck2 += [card2, card1]
        elif card1 > card2:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]

        d1 = tuple(deck1)
        d2 = tuple(deck2)
        if (d1, d2) in history:
            print(f'infinite, repeat: {(d1, d2)}')
            return deck1, []
        history.append((d1, d2))
    return deck1, deck2


# PART 1:
# deck1, deck2 = play_game(deck1, deck2)

# PART 2:
deck1, deck2 = play_game(deck1, deck2, recursion=True)
print(deck1, deck2)

if deck1:
    winner = deck1
else:
    winner = deck2

print(sum([x[0] * x[1] for x in zip(range(len(winner), 0, -1), winner)]))
