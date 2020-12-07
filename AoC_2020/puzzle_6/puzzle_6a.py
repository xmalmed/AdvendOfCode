def load_input(filename: str) -> list:
    with open(filename, 'r') as lines:
        input_data = []
        text = ''
        for line in lines:
            text += line.strip()
            if not line.strip():
                input_data.append(parse_input(text))
                text = ''
    input_data.append(parse_input(text))
    return input_data


def parse_input(text: str) -> set:
    return set(text)


if __name__ == "__main__":
    # group_answers = load_input("input_6.txt")
    group_answers = load_input("input_test.txt")

    total = 0

    for group in group_answers:
        total += len(group)

    print(total)
