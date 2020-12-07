def parse_input(text: str):
    int_2 = text.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    return int(int_2, 2)


def load_input():
    data = []
    with open("input_5.txt", 'r') as lines:
        for line in lines:
            data.append(parse_input(line.strip('\n')))
    return data


if __name__ == "__main__":
    seats = sorted(load_input())
    previous = seats[0] - 1
    print(f"max {seats[-1]}")
    for seat in seats:
        if seat - previous > 1:
            print(f"previous: {previous}, next {seat}")
        previous = seat
