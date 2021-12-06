from utils.puzzle import Puzzle


class FishType:
    def __init__(self):
        self.number = 0

    def get_number(self):
        return self.number

    def add_fishes(self, n):
        self.number += n

    def set_fishes(self, n):
        self.number = n

    def next_day(self):
        if self.age == 0:
            fish_types[8].add_fishes(self.number)
            self.age = 6
        else:
            if self.age == 7:
                fish_types[6]
            self.age -= 1


def next_day():
    new = fish_types[0].get_number()
    for i in range(0, 8):
        fish_types[i].set_fishes(fish_types[i + 1].get_number())

    fish_types[6].add_fishes(new)
    fish_types[8].set_fishes(new)


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    init_ages = map(int, data[0].split(","))
    fish_types = {cycle: FishType() for cycle in range(9)}
    for fish in init_ages:
        fish_types[fish].add_fishes(1)

    # part 1
    # for day in range(80):
    # part 2
    for day in range(256):
        next_day()
        total_fishes = sum([ft.get_number() for ft in fish_types.values()])
        print(f"After day {day + 1}: {total_fishes}")
