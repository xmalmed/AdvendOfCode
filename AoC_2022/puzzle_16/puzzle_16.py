from utils.puzzle import Puzzle


if __name__ == "__main__":
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input("input_test.txt")

    print("part1")
    # print(24*25 + 20*22 + 16*6 + 10*21 + 6*24) #1490
    print(27*8 + 24*19 + 20*23 + 17*13 + 14*15 + 6*10 + 2*18) # 1659

    print("part2")
    a = 23*8 + 20*19 + 16*23 + 13*13 + 10*15 + 2*10
    # b = 20*25 + 16*22 + 12*6 + 6*21 + 2*24          # 2369
    b = 22*6 + 19*25 + 15*22 + 6*21 + 2*24        #2382
    print(a+b)
