def load_input():
    passwd_list = []
    with open("input_2.txt", 'r') as passwd:
        # 6-16 b: bbbbbbbbbbbbbbbpb -> ['6', '16', 'b', 'bbbbbbbbbbbbbbbpb']
        for line in passwd:
            passwd_list.append((line.strip('\n').replace(':', '').replace('-', ' ')).split())
    return passwd_list


def count_valid_rules(data):
    valid_count = 0
    for [down, up, letter, password] in data:
        count = password.count(letter)
        if int(down) <= count <= int(up):
            valid_count += 1
    return valid_count


def count_valid_rules2(data):
    valid_count = 0
    for [first, second, letter, password] in data:
        count = (password[int(first) - 1] + password[int(second) - 1]).count(letter)
        if count == 1:
            valid_count += 1
    return valid_count


data = load_input()
print(count_valid_rules(data))
print(count_valid_rules2(data))
