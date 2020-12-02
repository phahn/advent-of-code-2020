import re


def part1(file):
    f = open(file)
    print(sum(1 for line in f.readlines() if match_part1(line)))


def part2(file):
    f = open(file)
    print(sum(1 for line in f.readlines() if match_part2(line)))


def match_part1(line):
    (min_amount, max_amount, character, password) = parse(line)
    actual_count = password.count(character)
    return actual_count >= min_amount and actual_count <= max_amount


def parse(line):
    mo = re.search("([0-9]+)\-([0-9]+)\s([a-z]+):\s([a-z]+)",
                   line)
    return (int(mo.group(1)), int(mo.group(2)), mo.group(3), mo.group(4))


def match_part2(line):
    (first_pos, last_post, character, password) = parse(line)
    first_pos_match = password[first_pos - 1] == character
    last_post_match = password[last_post - 1] == character
    return (first_pos_match and not last_post_match) or (not first_pos_match and last_post_match)


part1('day2/input.txt')
part2('day2/input.txt')
