from utils.puzzle import Puzzle


def draw(cycle, x, crt):
    if (cycle - 1) % 40 in (x - 1, x, x + 1):
        crt.append("#")
    else:
        crt.append(" ")


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    checkpoints = [20, 60, 100, 140, 180, 220]
    cycle = 0
    x = 1
    values = []
    crt = []

    for operation in data:
        cycle += 1
        draw(cycle, x, crt)
        if cycle in checkpoints:
            values.append(x * cycle)
        if operation != "noop":
            _, value = operation.split(" ")
            value = int(value)
            cycle += 1
            draw(cycle, x, crt)
            if cycle in checkpoints:
                values.append(x * cycle)
            x += value

    print(f"Sum of checkpoints: {sum(values)}")
    print("".join(crt[:40]))
    print("".join(crt[40:80]))
    print("".join(crt[80:120]))
    print("".join(crt[120:160]))
    print("".join(crt[160:200]))
    print("".join(crt[200:240]))
