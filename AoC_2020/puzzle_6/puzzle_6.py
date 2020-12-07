def load_input(filename: str) -> list:
    with open(filename, 'r') as lines:
        input_data = []
        group = []
        for line in lines:
            if not line.strip():
                input_data.append(group)
                group = []
            else:
                group.append(parse_input(line))
    input_data.append(group)
    return input_data


def parse_input(text: str) -> set:
    return set(text.strip())


if __name__ == "__main__":
    group_answers = load_input("input_6.txt")
    # group_answers = load_input("input_test.txt")

    total = 0

    for group in group_answers:
        total += len(set.intersection(*group))

    print(total)
