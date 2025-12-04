from utils.puzzle import Puzzle

def is_fake_id(id_str):
    """fake ID is 2 duplicate number, like 1010 (10)"""
    if len(id_str) % 2 != 0:
        return False
    half = len(id_str) // 2
    return id_str[:half] == id_str[half:]


def is_fake_id_2(id_str):
    """fake ID is n duplicate number, like 101010 (10)"""
    for n in range(1, len(id_str)//2 + 1):
        if len(id_str) % n == 0:
            times = len(id_str) // n
            if id_str == id_str[:n] * times:
                return True
    return False




if __name__ == '__main__':
    p = Puzzle(day=2, year=2025)
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    total = 0
    ids = data[0].split(',')
    for id in ids:
        start, end = id.split('-')
        for num in range(int(start), int(end)+1):
            # if is_fake_id(str(num)):
            if is_fake_id_2(str(num)):
                total += num

    print(total)

