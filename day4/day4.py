import re


def read_passports(file):
    f = open(file)
    passports = []
    passport = {}
    for line in f.readlines():
        if line == '\n':
            passports.append(passport)
            passport = {}
        else:
            tokens = line.split(' ')
            for token in tokens:
                key_value = token.strip().split(':')
                passport[key_value[0]] = key_value[1]
    passports.append(passport)
    return passports


def is_present(passport):
    expected_keys = set(['byr', 'iyr', 'eyr',  'hgt',
                         'hcl',  'ecl',  'pid'])
    passport_keys = set(passport.keys())
    return expected_keys.issubset(passport_keys)


def is_valid_byr(passport):
    return re.match('^\\d{4}$', passport['byr']) and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002


def is_valid_iyr(passport):
    return re.match('^\\d{4}$', passport['iyr']) and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020


def is_valid_eyr(passport):
    return re.match('^\\d{4}$', passport['eyr']) and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030


def is_valid_pid(passport):
    return re.match('^\\d{9}$', passport['pid'])


def is_valid_hgt(passport):
    m = re.match('(^\\d+)(in|cm)+$', passport['hgt'])
    if m == None:
        return False
    if m.group(2) == 'in':
        return int(m.group(1)) >= 59 and int(m.group(1)) <= 76
    if m.group(2) == 'cm':
        return int(m.group(1)) >= 150 and int(m.group(1)) <= 193
    return False


def is_valid_hcl(passport):
    return re.match('^#[0-9a-f]{6}$', passport['hcl'])


def is_valid_ecl(passport):
    ecl = passport['ecl']
    return ecl == 'amb' or ecl == 'blu' or ecl == 'brn' or ecl == 'gry' or ecl == 'grn' or ecl == 'hzl' or ecl == 'oth'


def part1():
    valid_passports = 0
    passports = read_passports('day4/input.txt')
    for passport in passports:
        if is_present(passport):
            valid_passports += 1
    print(valid_passports)


def part2():
    valid_passports = 0
    passports = read_passports('day4/input.txt')
    for passport in passports:
        if is_present(passport) and is_valid_byr(passport) and is_valid_iyr(passport) and is_valid_eyr(passport) and is_valid_pid(passport) and is_valid_ecl(passport) and is_valid_hcl(passport) and is_valid_hgt(passport):
            valid_passports += 1
    print(valid_passports)


part1()
part2()
