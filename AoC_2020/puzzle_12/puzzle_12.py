import numpy as np
from pathlib import Path
from parse import parse


class Ship:

    def __init__(self, x=0, y=0, orientation=np.array([1, 0])):
        self.x = x
        self.y = y
        self.orientation = orientation

    def rotation(self, direction: str, angle: int):
        sign = 1 if direction == 'R' else -1
        if angle == 90:
            self.orientation = np.dot(self.orientation, (sign * np.array([[0, -1], [1, 0]])))
        elif angle == 180:
            self.orientation = np.dot(self.orientation, (np.array([[-1, 0], [0, -1]])))
        else:
            self.orientation = np.dot(self.orientation, (sign * -1 * np.array([[0, -1], [1, 0]])))

    def move(self, side, value):
        if side == "N":
            self.y += value
        if side == "S":
            self.y -= value
        if side == "E":
            self.x += value
        if side == "W":
            self.x -= value
        if side == "F":
            self.x, self.y = self.orientation * value + np.array([self.x, self.y])

    def do_instruction(self, inst, value):
        if inst in ['R', 'L']:
            self.rotation(inst, value)
        else:
            self.move(inst, value)

    def manhattan_distance(self):
        print(f'Abs distance is: {abs(self.x) + abs(self.y)}')


class Waypoint(Ship):

    def rotation(self, direction: str, angle: int):
        sign = 1 if direction == 'R' else -1
        if angle == 90:
            self.x, self.y = np.dot(np.array([self.x, self.y]), (sign * np.array([[0, -1], [1, 0]])))
        elif angle == 180:
            self.x, self.y = np.dot(np.array([self.x, self.y]), (np.array([[-1, 0], [0, -1]])))
        else:
            self.x, self.y = np.dot(np.array([self.x, self.y]), (sign * -1 * np.array([[0, -1], [1, 0]])))


if __name__ == "__main__":
    with Path('input_12.txt').open() as file:
    # with Path('input_12_test.txt').open() as file:
        instructions = []
        for line in file:
            instructions.append(parse('{instruction}{value:d}', line.strip()))

    # part 1
    ship1 = Ship()
    for command in instructions:
        ship1.do_instruction(command['instruction'], command['value'])

    ship1.manhattan_distance()

    #part 2
    ship2 = Ship()
    waypoint = Waypoint(10, 1)
    for command in instructions:
        if command['instruction'] == 'F':
            ship2.do_instruction("N", waypoint.y * command['value'])
            ship2.do_instruction("E", waypoint.x * command['value'])
        else:
            waypoint.do_instruction(command['instruction'], command['value'])

    ship2.manhattan_distance()
