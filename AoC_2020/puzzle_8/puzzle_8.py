from copy import copy
from re import match


class Console:

    def __init__(self, position=0, accumulator=0):
        self.pointer = position
        self.acc = accumulator

    def jump(self, value: int):
        self.pointer += value

    def accumulate(self, value: int):
        self.acc += value
        self.pointer += 1

    def nop(self, value: int):
        self.pointer += 1

    def run(self, instructions):
        inst = instructions[self.pointer]
        while inst:
            instructions[self.pointer] = False
            if inst[0] == 'acc':
                self.accumulate(inst[1])
            elif inst[0] == 'jmp':
                self.jump(inst[1])
            elif inst[0] == 'nop':
                self.nop(inst[1])
            elif inst == 'end':
                print(f'END: accumulator is: {self.acc}')
                return True
            else:
                print(f'broken... {self.pointer}')
            inst = instructions[self.pointer]

        print("No success.")
        return self.acc


def parse_input(text: str):
    (inst, value) = match(r'(acc|jmp|nop) ([+-]?\d+)', text).groups()
    return inst, int(value)


def load_input(filename):
    data = []
    with open(filename, 'r') as lines:
        for line in lines:
            data.append(parse_input(line.strip('\n')))
    return data


if __name__ == "__main__":
    instructions = load_input("input_8.txt")
    instructions.append("end")
    con = Console()
    acc = con.run(copy(instructions))

    print(f'Accumulator is: {acc}')

    for i in range(len(instructions) - 1):
        con = Console()
        if instructions[i][0] == 'acc':
            continue
        if instructions[i][0] == 'jmp':
            new_inst = copy(instructions)
            new_inst[i] = ('nop', instructions[i][1])
        else:
            new_inst = copy(instructions)
            new_inst[i] = ('jmp', instructions[i][1])

        acc = con.run(new_inst)
        if acc == True:
            break
