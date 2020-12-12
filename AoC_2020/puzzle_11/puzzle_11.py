from copy import deepcopy
from itertools import product


def load_input(filename="input_11.txt"):
    file_lines = []
    with open(filename, 'r') as lines:
        for line in lines:
            file_lines.append(list("," + line.strip('\n') + ","))
    file_lines.insert(0, list("," * len(file_lines[0])))
    file_lines.append(list("," * len(file_lines[0])))
    return file_lines


def next_seat(boat):
    x = y = 1
    while (y <= len(boat) - 3) or (x <= len(boat[0]) - 3):
        yield x, y
        if x <= len(boat[0]) - 3:
            x += 1
        else:
            x = 1
            y += 1
    yield x, y


def adj_seats(x: int, y: int, boat) -> str:
    return boat[y - 1][x - 1:x + 2] + [boat[y][x - 1]] + [boat[y][x + 1]] + boat[y + 1][x - 1:x + 2]


def follow_direction(x, y, dx, dy, boat):
    while True:
        x += dx
        y += dy
        seat = boat[y][x]
        if seat in '#L,':
            return seat


def visible_seats(x: int, y: int, boat) -> str:
    adj = adj_seats(x, y, boat)
    if adj.count('.') == 0:
        return adj
    else:
        seats = ''
        for direc in product([-1,0, 1], [-1,0, 1]):
            if direc != (0, 0):
                seats += follow_direction(x, y, direc[0], direc[1], boat)
        return seats


def evaluate_seat(seats_string: str, center: str):
    count = seats_string.count("#")
    if count >= 4:
        return 'L'
    elif count == 0:
        return '#'
    else:
        return center


def evaluate_seat_new(seats_string: str, center: str):
    count = seats_string.count("#")
    if count >= 5:
        return 'L'
    elif count == 0:
        return '#'
    else:
        return center


def count_boat(boat, draw=False):
    total = 0
    for line in boat:
        total += line.count('#')
        if draw:
            print("".join(line))
    return total


if __name__ == "__main__":
    boat = load_input("input_11_test.txt")
    # boat = load_input("input_11.txt")

    # part 1
    counter = 0
    while True:
        new_boat = deepcopy(boat)
        for (x, y) in next_seat(boat):
            if boat[y][x] == '.':
                continue
            new_boat[y][x] = evaluate_seat(adj_seats(x, y, boat), boat[y][x])
        if new_boat == boat:
            break
        counter += 1
        boat = new_boat

    print(count_boat(new_boat))

    # part 2
    # boat = load_input("input_11_test.txt")
    boat = load_input("input_11.txt")
    counter = 0
    print(f'Kolo {counter}')
    print(count_boat(boat, True))
    while True:
        new_boat = deepcopy(boat)
        for (x, y) in next_seat(boat):
            if boat[y][x] == '.':
                continue
            new_boat[y][x] = evaluate_seat_new(visible_seats(x, y, boat), boat[y][x])
        if new_boat == boat:
            break
        counter += 1
        boat = new_boat
        print(f'Kolo {counter}')
        print(count_boat(boat, True))

    print(count_boat(new_boat))
