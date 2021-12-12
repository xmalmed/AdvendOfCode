from utils.puzzle import Puzzle
from numpy import array
from itertools import product

edge = float('-inf')
surrounding = list(product([-1, 0, 1], [-1, 0, 1]))
surrounding.remove((0, 0))

def charge_surroundings(x, y):
    for s in surrounding:
        if octopuses[y + s[0], x + s[1]] > 0:
            octopuses[y + s[0], x + s[1]] += 1


if __name__ == '__main__':
    p = Puzzle()
    data = p.load_input(string=True)
    # data = p.load_input('input_test.txt', string=True)


    octopuses = [[edge]*12]
    for line in data:
        octopuses.append([edge] + [int(ch) for ch in line] + [edge])
    octopuses.append([edge]*12)
    octopuses = array(octopuses)
    #
    # print('Step 0')
    # print(octopuses)

    total_flashes = 0
    for step in range(1, 100000):
        print('Step: ', step)
        octopuses += 1
        # print(octopuses)
        flash = True
        while flash:
            # charged = octopuses[octopuses >= 9]
            flash = False
            for y in range(1, 11):
                for x in range(1, 11):
                    if octopuses[y, x] >= 10:
                        octopuses[y, x] = 0
                        charge_surroundings(x, y)
                        total_flashes += 1
                        flash = True

        if len(octopuses[octopuses >= 1]) == 0:
            print("Synchronous step: ", step)
            break

        if step == 100:
            print(total_flashes)
