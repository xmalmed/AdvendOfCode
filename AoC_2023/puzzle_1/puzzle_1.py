from utils.puzzle import Puzzle
import re

if __name__ == '__main__':
    p = Puzzle()
    data = p.load_input()
    # data = p.load_input('input_test.txt')

    total = 0
    for d in data:
        x = re.search(r'[0-9]', d)
        y = re.search(r'.*([0-9])', d)
        total += int(x.group() + y.groups()[0])

    print(total)

    total2 = 0
    for d in data:
        x = re.search(r'[0-9]|(one|two|three|four|five|six|seven|eight|nine)', d)
        y = re.search(r'.*([0-9]|(one|two|three|four|five|six|seven|eight|nine))', d)
        x = x.group().replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9')
        y = y.groups()[0].replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9')
        total2 += int(x + y)

    print(total2)
