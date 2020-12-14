from copy import deepcopy
from parse import parse
from pathlib import Path

MEMORY = {}


def store_data(address, number, mask):
    construct = list(mask)
    digits = list("{0:036b}".format(number))
    result = []
    for (d, m) in zip(digits, construct):
        if m == 'X':
            result.append(d)
        else:
            result.append(m)
    MEMORY[address] = int(''.join(result), 2)


def get_addresses(address, mask):
    bin_address = list("{0:036b}".format(address))
    construct = list(mask)
    result = []
    for (a, m) in zip(bin_address, construct):
        if m == '0':
            result.append(a)
        else:
            result.append(m)
    addresses = [result]
    for x in range(result.count('X')):
        new_addresses = []
        for a in addresses:
            i = a.index('X')
            a[i] = '0'
            new_addresses.append(a)
            b = a.copy()
            b[i] = '1'
            new_addresses.append(b)
        addresses = deepcopy(new_addresses)
    return addresses


if __name__ == "__main__":
    filename = "input_14.txt"
    with Path(filename).open() as file:
        for line in file:
            data = parse('{instruction} = {value}', line.strip())

            if data['instruction'] == 'mask':
                mask = data['value']
            else:
                address = parse('mem[{mem:d}]', data['instruction'])['mem']
                num = int(data['value'])
                # part 1
                # store_data(address, num, mask)
                # part 2
                for adr in get_addresses(address, mask):
                    MEMORY[int(''.join(adr), 2)] = num

    print(sum(MEMORY.values()))
