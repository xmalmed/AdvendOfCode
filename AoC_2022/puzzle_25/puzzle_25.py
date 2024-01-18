from utils.puzzle import Puzzle


def get_snafu(x):
    snafu = ''
    while x:
        r = x % 5
        match r:
            case 3:
                snafu = '=' + snafu
                x = x // 5 + 1
            case 4:
                snafu = '-' + snafu
                x = x // 5 + 1
            case _:
                snafu = str(r) + snafu
                x = x // 5
                
    return snafu
            
            
if __name__ == '__main__':
    p = Puzzle(day=21, year=2022)
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    total = 0
    for num in data:
        for i, ch in enumerate(num[::-1]):
            match ch:
                case '-':
                    total += 5**i * -1
                case '=':
                    total += 5**i * -2
                case _:
                    total += 5**i * int(ch)

    print(total, get_snafu(total))

    # for i in range(1, 21):
    #     print(i, get_snafu(i))
    #
    # print(314159265, get_snafu(314159265))

