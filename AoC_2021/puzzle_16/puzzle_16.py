from utils.puzzle import Puzzle
from math import prod


def decode_package(cursor, input, versions):
    read = 3
    version = int(input[cursor : cursor + read], 2)
    cursor += read
    versions.append(version)

    read = 3
    type = int(input[cursor : cursor + read], 2)
    cursor += read
    # print('version ', version, '   type ', type)

    if type == 4:
        next_number = True
        number2 = ""
        while next_number:
            read = 1
            if int(input[cursor : cursor + read], 2) == 0:
                next_number = False
            cursor += read
            read = 4
            number2 += input[cursor : cursor + read]
            cursor += read
        value = int(number2, 2)
        return cursor, value
    else:
        read = 1
        id_type = int(input[cursor : cursor + read], 2)
        cursor += read
        values = []
        if id_type == 0:
            read = 15
            sub_package_len = int(input[cursor : cursor + read], 2)
            cursor += read
            stop = cursor + sub_package_len
            while cursor < stop:
                cursor, value = decode_package(cursor, input, versions)
                values.append(value)
        elif id_type == 1:
            read = 11
            sub_package_number = int(input[cursor : cursor + read], 2)
            cursor += read
            for _ in range(sub_package_number):
                cursor, value = decode_package(cursor, input, versions)
                values.append(value)

        if type == 0:
            value = sum(values)
        elif type == 1:
            value = prod(values)
        elif type == 2:
            value = min(values)
        elif type == 3:
            value = max(values)
        elif type == 5:
            value = 1 if values[0] > values[1] else 0
        elif type == 6:
            value = 1 if values[0] < values[1] else 0
        else:
            value = 1 if values[0] == values[1] else 0
        return cursor, value


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")
    for line in data:
        package = line
        versions = []
        number10 = int(package, 16)
        first_package = "{0:0>{1}b}".format(number10, len(package) * 4)

        cursor, value = decode_package(0, first_package, versions)

        # print(versions)
        print("value: ", value, "    sum of versions: ", sum(versions))
