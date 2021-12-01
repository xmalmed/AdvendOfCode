if __name__ == "__main__":
    filename = "puzzle_1_input.txt"
    data = []

    last_depth = float("inf")
    count = 0
    with open(filename, "r") as input_file:
        for line in input_file:
            depth = int(line)
            if last_depth < depth:
                count += 1

            last_depth = depth
            data.append(depth)

    print("number of increases of depth is: ", count)

    last_depth = float("inf")
    count = 0
    for i, d in enumerate(data):
        depth = sum(data[i : i + 3])
        if depth > last_depth:
            count += 1

        last_depth = depth

    print("number of increases in sliding window is: ", count)
