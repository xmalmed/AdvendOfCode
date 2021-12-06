from utils.puzzle import Puzzle


class FishType:
    def __init__(self):
        self.number = 0


def next_day():
    new = fish_types[0].number
    for i in range(0, 8):
        fish_types[i].number = fish_types[i + 1].number

    fish_types[6].number += new
    fish_types[8].number = new


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    init_ages = map(int, data[0].split(","))
    fish_types = {cycle: FishType() for cycle in range(9)}
    for fish in init_ages:
        fish_types[fish].number += 1

    # part 1
    # for day in range(80):
    # part 2
    for day in range(256):
        next_day()
        total_fishes = sum([ft.number for ft in fish_types.values()])
        print(f"After day {day + 1}: {total_fishes}")
