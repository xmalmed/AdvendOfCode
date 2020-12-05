INPUT2 = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,5,23,1,23,9,27,2,27,6,31,1,31,6,35,2,35,9,39,1,6,39,43,2,10,43,47,1,47,9,51,1,51,6,55,1,55,6,59,2,59,10,63,1,6,63,67,2,6,67,71,1,71,5,75,2,13,75,79,1,10,79,83,1,5,83,87,2,87,10,91,1,5,91,95,2,95,6,99,1,99,6,103,2,103,6,107,2,107,9,111,1,111,5,115,1,115,6,119,2,6,119,123,1,5,123,127,1,127,13,131,1,2,131,135,1,135,10,0,99,2,14,0,0]
# INPUT = [1,9,10,3,2,3,11,0,99,30,40,50]


def read(index):
    return INPUT[INPUT[index]]


def add(index: int):
    a = read(index + 1)
    b = read(index + 2)
    INPUT[INPUT[index + 3]] = a + b
    return index + 4


def multi(index: int):
    a = read(index + 1)
    b = read(index + 2)
    INPUT[INPUT[index + 3]] = a * b
    return index + 4


def exit():
    print(INPUT[0])
    if INPUT[0] == 19690720:
        exit()
    return False


def operation(index: int):
    if INPUT[index] == 1:
        next = add(index)
    elif INPUT[index] == 2:
        next = multi(index)
    elif INPUT[index] == 99:
        next = exit()
    else:
        print(INPUT[index])
        next = False

    return next


def main_loop(index):
    while index is not False:
        # print(INPUT)
        index = operation(index)


for i in range(100):
    for j in range(100):
        INPUT = INPUT2.copy()
        INPUT[1] = i
        INPUT[2] = j
        print(i, j)
        main_loop(0)

# main_loop(0)
