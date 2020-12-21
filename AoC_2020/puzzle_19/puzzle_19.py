from pyformlang.cfg import Production, Variable, Terminal, CFG
from parse import parse
from pathlib import Path

# filename = "input_19_test.txt"
filename = "input_19.txt"
tests = []
vars = {}
ters = {}
productions = []


def create_production(id, l):
    return Production(vars[id], [vars[x] for x in l])


for i in range(132):
    vars[i] = Variable(i)

with Path(filename).open() as file:
    while line := file.readline().strip():
        data = parse('{id:d}: {rules}', line)
        if data['rules'] == '"a"':
            ters["a"] = Terminal("a")
            productions.append(Production(vars[data['id']], [ters["a"]]))
        elif data['rules'] == '"b"':
            ters["b"] = Terminal("b")
            productions.append(Production(vars[data['id']], [ters["b"]]))
        elif '|' in data['rules']:
            for r in data['rules'].split("|"):
                productions.append(create_production(data['id'], [int(x) for x in r.split()]))
        else:
            productions.append(create_production(data['id'], [int(x) for x in data['rules'].split()]))

    while line := file.readline().strip():
        tests.append(line)

# Creation of the Context-Free Grammar
# PART 1
cfg1 = CFG(set(vars.values()), set(ters.values()), vars[0], set(productions))

# PART 2
productions.append(create_production(8, [42, 8]))
productions.append(create_production(11, [42, 11, 31]))
cfg2 = CFG(set(vars.values()), set(ters.values()), vars[0], set(productions))

valids = []
for test in tests:
    # valids.append(cfg1.contains([ters[char] for char in test]))
    valids.append(cfg2.contains([ters[char] for char in test]))

print(valids.count(True))
