from utils.puzzle import Puzzle

if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    # part 1
    count = 0
    for line in [d.split(" | ") for d in data]:
        for digit in line[1].split():
            if len(digit) in [2, 3, 4, 7]:
                count += 1

    print("Count of numbers 1, 4, 7, and 8 is: ", count)

    # part 2
    total = 0
    for line in [d.split(" | ") for d in data]:
        digit_dictionary = list(map(set, line[0].split()))
        digit_dictionary.sort(key=lambda x: len(x))
        res = []
        for digit in line[1].split():
            if len(digit) == 2:
                res.append(1)
            elif len(digit) == 3:
                res.append(7)
            elif len(digit) == 4:
                res.append(4)
            elif len(digit) == 5:
                if digit_dictionary[0].issubset(set(digit)):
                    res.append(3)
                elif len(digit_dictionary[2].intersection(set(digit))) == 3:
                    res.append(5)
                else:
                    res.append(2)
            elif len(digit) == 6:
                if digit_dictionary[2].issubset(set(digit)):
                    res.append(9)
                elif digit_dictionary[0].issubset(set(digit)):
                    res.append(0)
                else:
                    res.append(6)
            else:
                res.append(8)

        number = int("".join([str(x) for x in res]))
        total += number

    print('Sum of all decoded 4-digit numbers: ', total)
