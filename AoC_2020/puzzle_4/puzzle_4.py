from parse import parse
from re import match
# import puzzle_4

def load_input():
    file_lines = ['']
    # with open("input_4_example.txt", 'r') as lines:
    with open("input_4.txt", 'r') as lines:
        for line in lines:
            if data := line.strip():
                file_lines[-1] = ' '.join([file_lines[-1], data])
            else:
                file_lines[-1] = file_lines[-1].split()
                file_lines.append('')
    file_lines[-1] = file_lines[-1].split()
    return file_lines


def validate_passport(pp: list):
    if len(pp) == 8:
        return True
    elif len(pp) == 7 and not any("cid:" in field for field in pp):
        return True
    else:
        return False

passports = load_input()
print(passports)

valid_count = 0
for pp in passports:
    if validate_passport(pp):
        valid_count += 1
    else:
        print(pp)

print(valid_count)

# parse("byr:{}
# iyr:{}
# eyr:{}
# hgt:{}
# hcl:{}
# ecl:{}
# pid:{}
# cid:{} )
