import pytest
import puzzle_4


def test_parse_passport():
    data = puzzle_4.parse_input("hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022")
    assert data == {"byr": "2001", "iyr": "2015", "eyr": "2022", "hgt": "164cm", "hcl": "#888785", "ecl": "hzl",
                    "pid": "545766238", "cid": "88"}


@pytest.mark.parametrize("passport_data,valid", [
    ({"byr": "2001", "iyr": "2015", "eyr": "2022", "hgt": "164cm", "hcl": "#888785", "ecl": "hzl",
      "pid": "545766238", "cid": "88"}, True),
    ({"byr": "2001", "iyr": "2015", "eyr": "2022", "hgt": "164cm", "hcl": "#888785", "ecl": "hzl",
      "pid": "545766238"}, True),
    ({"byr": "2001", "iyr": "2015", "eyr": "2022", "hgt": "164cm", "hcl": "#888785", "ecl": "hzl",
      "cid": "88"}, False)])
def test_passport_fields_exist(passport_data, valid):
    assert puzzle_4.validate_passport_by_fields(passport_data) == valid


@pytest.mark.parametrize("passport_data,valid",
                         [(p, True) for p in puzzle_4.load_input("input_4_pass.txt")] +
                         [(p, False) for p in puzzle_4.load_input("input_4_fail.txt")])
def test_validate_passport(passport_data, valid):
    # fail_data = puzzle_4.load_input("input_4_fail.txt")
    # pass_data = puzzle_4.load_input("input_4_pass.txt")
    # for passport in pass_data:
    #     assert puzzle_4.validate_passport(passport), f"Failing PASS case: {passport}"
    # for passport in fail_data:
    #     assert not puzzle_4.validate_passport(passport), f"Failing FAIL case: {passport}"
    assert puzzle_4.validate_passport(passport_data) == valid
