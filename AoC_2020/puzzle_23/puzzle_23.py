import time
# input = '389125467'     # test
input = '496138527'  # real (start only)

cups = [int(x) for x in input]

def run_game(cups, moves):
    mod = len(cups)
    pick = 3

    cc = 0  # current cup
    for j in range(1, moves + 1):
        if j % 10000 == 0:
            print(f'--- move {j} --- {time.process_time() - start_time} seconds')
            # print(f'index: {cc}, value: {cups[cc]}')
        picked = [cups[(cc + 1 + i) % mod] for i in range(pick)]
        cc_value = cups[cc]
        dc_value = cc_value - 1
        if dc_value == 0:
            dc_value = mod
        while dc_value in picked:
            dc_value -= 1
            if dc_value == 0:
                dc_value = mod

        if cc + 3 < mod:
            del(cups[cc+1:cc+4])
        else:
            for value in picked:
                cups.remove(value)
        dc = cups.index(dc_value)

        while picked:
            cups.insert(dc + 1, picked.pop())

        if dc > cc:
            cc = cc + 1
        else:
            if cc + 4 < mod:
                cc += 4
            else:
                cc = (cups.index(cc_value) + 1) % mod

    return cc, cups

# part 1
cc, cups = run_game(cups.copy(), 100)

print(f'final: {cups}')
print(f'index: {cc}, value: {cups[cc]}')
temp = ''.join(map(str, cups)).split('1')
print(temp[1] + temp[0])

# part 2
cups += list(range(len(cups) + 1, 1000000 + 1))

start_time = time.process_time()
cc, cups = run_game(cups, 10000000)
c0 = cups.index(1)
c1 = cups[(c0 + 1) % 1000000]
c2 = cups[(c0 + 2) % 1000000]
print(f'after 1 cup: {c1} * {c2} = {c1 * c2}')
print(f'cup around 1: {cups[c0 - 2 : c0 + 5]}')

