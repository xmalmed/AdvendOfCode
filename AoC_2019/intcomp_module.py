from collections import defaultdict

class IntComp:
    '''IntComp processor'''

    def __init__(self, program=[], index=0, inputs=[]):
        d = dict(enumerate(program))
        self.program = defaultdict(lambda: 0, d)
        self.index = index
        self.inputs = inputs
        self.index_base = 0

    def get_value(self, index, mode):
        if mode == 0:
            return self.program[self.program[index]]
        elif mode == 1:
            return self.program[index]
        elif mode == 2:
            return self.program[self.index_base + self.program[index]]
        else:
            raise ValueError("Cannot read in the program.")

    def add(self, index: int, c, b, a):
        x = self.get_value(index + 1, c)
        y = self.get_value(index + 2, b)
        where = self.program[index + 3]
        self.program[where] = x + y
        # print(where, x + y)
        return index + 4

    def multi(self, index: int, c, b, a):
        x = self.get_value(index + 1, c)
        y = self.get_value(index + 2, b)
        where = self.program[index + 3]
        self.program[where] = x * y
        # print(where, x * y)
        return index + 4

    def insert(self, index: int, value: int, c):
        if c == 2:
            where = self.index_base + self.program[index + 1]
        else:
            where = self.program[index + 1]

        self.program[where] = value
        # print(where, value)
        return index + 2

    def output(self, index: int, c):
        if c == 0:
            where = self.program[index + 1]
        elif c == 1:
            where = index + 1
        elif c == 2:
            where = self.index_base + self.program[index + 1]
        else:
            print("Bad mode.")
        return index + 2, self.program[where]

    def jump_if_true(self, index, c, b):
        x = self.get_value(index + 1, c)
        if x != 0:
            return self.get_value(index + 2, b)
        else:
            return index + 3

    def jump_if_false(self, index, c, b):
        x = self.get_value(index + 1, c)
        if x == 0:
            return self.get_value(index + 2, b)
        else:
            return index + 3

    def less_than(self, index, c, b, a):
        x = self.get_value(index + 1, c)
        y = self.get_value(index + 2, b)
        where = self.program[index + 3]
        if x < y:
            self.program[where] = 1
        else:
            self.program[where] = 0
        # print(where, self.program[where])
        return index + 4

    def equals(self, index, c, b, a):
        x = self.get_value(index + 1, c)
        y = self.get_value(index + 2, b)
        where = self.program[index + 3]
        if x == y:
            self.program[where] = 1
        else:
            self.program[where] = 0
        # print(where, self.program[where])
        return index + 4

    def change_base(self, index, c):
        change = self.get_value(index + 1, c)
        self.index_base += change
        return index + 2

    def exit(self):
        return None, False

    def get_input(self):
        if self.inputs == []:
            self.inputs.append(
                int(input("Input integer: "))
            )
        return self.inputs.pop(0)

    def next_operation(self):
        """Main function => public?"""
        index = self.index
        opcode, c, b, a = self.get_params(self.program[index])
        output = None

        if opcode == 1:
            next_index = self.add(index, c, b, a)
        elif opcode == 2:
            next_index = self.multi(index, c, b, a)
        elif opcode == 3:
            value = self.get_input()
            next_index = self.insert(index, value, c)
        elif opcode == 4:
            next_index, output = self.output(index, c)
        elif opcode == 5:
            next_index = self.jump_if_true(index, c, b)
        elif opcode == 6:
            next_index = self.jump_if_false(index, c, b)
        elif opcode == 7:
            next_index = self.less_than(index, c, b, a)
        elif opcode == 8:
            next_index = self.equals(index, c, b, a)
        elif opcode == 9:
            next_index = self.change_base(index, c)
        elif opcode == 99:
            next_index, output = self.exit()
        else:
            raise ValueError(f"Program opcode error, {self.program[index]}.")

        self.index = next_index
        return output

    def get_params(self, opcode):
        # print(self.index, self.index_base, opcode)
        if opcode <= 99:
            return opcode, 0, 0, 0
        else:
            mode = opcode // 100
            opcode = opcode % 100
            c = int(str(mode)[-1])
            if len(str(mode)) == 3:
                a = int(str(mode)[-3])
                b = int(str(mode)[-2])
            elif len(str(mode)) == 2:
                b = int(str(mode)[-2])
                a = 0
            else:
                b = a = 0
        return opcode, c, b, a
