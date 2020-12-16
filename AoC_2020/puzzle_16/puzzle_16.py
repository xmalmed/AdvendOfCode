from parse import parse
from pathlib import Path

filename = "input_16.txt"

with Path(filename).open() as file:
    first_block = True
    last_block = False
    rules = []
    all_tickets = []
    for line in file:
        if line.strip() == "" and not first_block:
            last_block = True
            continue
        if line.strip() == "":
            first_block = False
            continue
        if first_block:
            rules.append(parse("{name}: {s1:d}-{e1:d} or {s2:d}-{e2:d}", line.strip()))
            # data = parse("{name}: {s1:d}-{e1:d} or {s2:d}-{e2:d}", line.strip())
            # rules.append((data['s1'], data['e1'], data['s2'], data['e2']))
        if not first_block and not last_block:
            if line.strip() != 'your ticket:':
                my_ticket = [int(number) for number in line.strip().split(',')]
        if last_block:
            if line.strip() != "nearby tickets:":
                all_tickets.append([int(number) for number in line.strip().split(',')])

# invalid tickets:
total_invalid = 0
invalid_tickets = []
for ticket in all_tickets:
    for number in ticket:
        # expect multiple invalid numbers? No
        if not any([r['s1'] <= number <= r['e1'] or r['s2'] <= number <= r['e2'] for r in rules]):
            total_invalid += number
            invalid_tickets.append(ticket)
            break
print(f'Total invalid numbers: {total_invalid}')

print(len(all_tickets))
print(len(invalid_tickets))
valid_tickets = [ticket for ticket in all_tickets if ticket not in invalid_tickets]
print(len(valid_tickets))

table_rule_column = []

for rule in rules:
    table_rule_column.append([])
    for column in range(len(valid_tickets[0])):
        apply_rules = [
            rule['s1'] <= number <= rule['e1'] or rule['s2'] <= number <= rule['e2'] for number in
            [row[column] for row in valid_tickets]
        ]
        table_rule_column[-1].append(all(apply_rules))

for i in range(20):
    print(''.join(['#' if x else ' ' for x in table_rule_column[i]]))

'''r15: s8
r9: s11
r11: s16
r18: s7
r20: s13
r8: s2
r2: s12
r3: s18
r1: s6
r5: s15
r6: s14
r4: s20
...'''

print(f'Departure *: {my_ticket[5] * my_ticket[11] * my_ticket[17] * my_ticket[19] * my_ticket[14] * my_ticket[13]}')