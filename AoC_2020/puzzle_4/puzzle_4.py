from re import match


def load_input(filename: str) -> list:
    with open(filename, 'r') as lines:
        input_data = []
        text = ''
        for line in lines:
            text += line
            if not line.strip():
                input_data.append(parse_input(text))
                text = ''
    input_data.append(parse_input(text))
    return input_data


def parse_input(text: str) -> dict:
    data = [match('([a-z]{3}):(.+)', field).groups() for field in text.split()]
    return dict(data)


def validate_passport_by_fields(passport_data: dict):
    if len(passport_data) == 8:
        return True
    elif len(passport_data) == 7 and ("cid" not in passport_data):
        return True
    else:
        return False


def validate_passport(pp: dict):
    if not 1920 <= int(pp['byr']) <= 2002:
        return False
    if not 2010 <= int(pp['iyr']) <= 2020:
        return False
    if not 2020 <= int(pp['eyr']) <= 2030:
        return False
    if not valid_height(pp['hgt']):
        return False
    if not match(r'#[0-9a-f]{6}', pp['hcl']):
        return False
    if pp['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not match(r'\d{9}$', pp['pid']):
        return False
    return True


def valid_height(height):
    try:
        (value, unit) = match(r'(\d+)(cm|in)', height).groups()
    except AttributeError:
        return False
    if unit == 'cm' and 150 <= int(value) <= 193:
        return True
    if unit == 'in' and 59 <= int(value) <= 76:
        return True
    return False


if __name__ == "__main__":

    passports = load_input("input_4.txt")

    valid_count_by_fields = 0
    valid_count = 0
    for pp in passports:
        if validate_passport_by_fields(pp):
            valid_count_by_fields += 1
            if validate_passport(pp):
                valid_count += 1
            else:
                print(f"invalid data {pp}")
        else:
            print(f"missing fields {pp}")

    print(f"Valid fields: {valid_count_by_fields} and valid data: {valid_count}")
