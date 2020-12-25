from time import process_time
# input = '389125467'     # test
input = '496138527'  # real (start only)
cups_order = [int(x) for x in input]


class Cup(object):
    cup_max = 0

    def __init__(self, value: int, prev=None, next=None, dc=None):
        self.value = value
        self.prev = prev
        self.next = next
        self.dc = dc
        Cup.cup_max += 1

    def find_dc(self):
        if not self.dc:
            if self.value == 1:
                looking_for = Cup.cup_max
            else:
                looking_for = self.value - 1
            cup = self
            while True:
                cup = cup.prev
                if cup.value == looking_for:
                    self.dc = cup
                    break

    def move_next_cup_after_destination(self, dest):  # dest must not be in 3 next cups
        # ignore possition
        moved_cup = self.next

        self.next = self.next.next  # fix current cup:
        self.next.prev = self  # fix next next cup:
        # fix moving cup
        moved_cup.prev = dest
        moved_cup.next = dest.next

        moved_cup.next.prev = moved_cup  # fix next cup after moved one
        dest.next = moved_cup  # fix prev cup before moved one

    def play_move(self):
        next3 = [self.next, self.next.next, self.next.next.next]
        dest = self.dc
        while dest in next3:
            dest = dest.dc
        for i in range(3):
            self.move_next_cup_after_destination(dest)
            dest = next3[i]


def initialize(part2=False) -> list:
    Cup.cup_max = 0
    cups = [Cup(val) for val in cups_order]
    if part2:
        milion = 10**6
        add_cups = [Cup(val) for val in range(len(cups) + 1, milion + 1)]
        cups = cups + add_cups
    for pos, cup in enumerate(cups):
        cup.next = cups[(pos + 1) % len(cups)]
        cup.prev = cups[(pos - 1) % len(cups)]
    for cup in cups:
        cup.find_dc()
    return cups


# PART 1
cups = initialize()
cc = cups[0]

for _ in range(100):
    cc.play_move()
    cc = cc.next

output = []
for _ in range(len(cups)):
    output.append(str(cc.value))
    cc = cc.next

res = ''.join(output).split('1')
print(res[1] + res[0], " from ", ''.join(output))


# PART 2
print('part 2')
init_time = process_time()
cups = initialize(part2=True)
cc = cups[0]
start_time = process_time()
print(f'init time: {start_time - init_time}')

for j in range(10 ** 7):
    if j % 100000 == 0:
        print(f'--- done {j/100000} % ---: {process_time() - start_time}')
    cc.play_move()
    cc = cc.next

print(cups[3].value)
print(cups[3].next.value)
print(cups[3].next.next.value)
print(cups[3].next.value * cups[3].next.next.value)
