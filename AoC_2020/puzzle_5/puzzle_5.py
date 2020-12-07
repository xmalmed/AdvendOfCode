def load_input():
    file_lines = []
    with open("input_4.txt", 'r') as lines:
        for line in lines:
            file_lines.append(line.strip('\n'))  # replace(':', '') replace('-', ' ')) split()
    return file_lines
