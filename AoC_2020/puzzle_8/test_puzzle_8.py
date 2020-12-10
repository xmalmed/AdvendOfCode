from copy import copy

import pytest
from puzzle_8 import Console

INSTRUCTIONS = [('nop', 0), ('acc', 1), ('jmp', 4), ('acc', 3), ('jmp', -3), ('acc', -99), ('acc', 1), ('jmp', -4),
                ('acc', 6), 'end']

@pytest.fixture()
def console():
    return Console(4, -2)


def test_console_state(console):
    assert console.pointer == 4
    assert console.acc == -2


def test_jump(console):
    console.jump(-1)
    assert console.pointer == 3
    assert console.acc == -2


def test_accumulator(console):
    console.accumulate(3)
    assert console.pointer == 5
    assert console.acc == 1


def test_nop(console):
    console.nop(-3)
    assert console.pointer == 5
    assert console.acc == -2


def test_first_console_run():
    new_instructions = copy(INSTRUCTIONS)
    assert Console().run(new_instructions) == 5


def test_fixed_console_run():
    new_instructions = copy(INSTRUCTIONS)
    new_instructions[7] = ('nop', new_instructions[7][1])
    assert Console().run(new_instructions) == True
