from utils.puzzle import Puzzle
import numpy as np

if __name__ == '__main__':
    p = Puzzle(day=4, year=2025)
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    size = len(data[0])
    boards = []
    boards.append([0]*(size+2))
    for l in data:
        a = [0]
        for ch in l:
            if ch == "@":
                a.append(1)
            else:
                a.append(0)
        a.append(0)
        boards.append(a)
    boards.append([0] * (size+2))
    boards = np.array(boards)

    print()
    count = 0

    for i in range(1, boards.shape[0]-1):
        for j in range(1, boards.shape[1]-1):
            if boards[i,j] == 1 and  sum(sum(boards[i-1:i+2, j-1:j+2])) < 5:
                count+=1

    print(count)

    count2 = 0
    removing = True
    while removing:
        removing = False
        for i in range(1, boards.shape[0] - 1):
            for j in range(1, boards.shape[1] - 1):
                if boards[i, j] == 1 and (boards[i - 1:i + 2, j - 1:j + 2]).sum() < 5:
                    count2 += 1
                    boards[i, j] = 0
                    removing = True


    print(count2)