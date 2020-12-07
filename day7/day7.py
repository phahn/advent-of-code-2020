def parse_bags(file):
    bags = {}
    f = open(file)
    for line in f.readlines():
        bag = {'rules': []}
        tokens = line.split('bags contain')
        bag['color'] = tokens[0].strip()
        rules = tokens[1].split(',')
        for rule in rules:
            rule = rule.strip().replace('.', '').split(" ")
            if rule[0] != 'no':
                r = {}
                r['amount'] = int(rule[0])
                r['color'] = rule[1] + " " + rule[2]
                bag['rules'].append(r)

        bags[bag['color']] = bag
    return bags


def is_valid(bags, color):
    return bags[color]['color'] == 'shiny gold' or any(is_valid(bags, r['color']) for r in bags[color]['rules'])


def sum_bags(bags, color):
    return 1 + sum(r['amount'] * sum_bags(bags, r['color'])
                   for r in bags[color]['rules'])


def part1():
    cnt = 0
    bags = parse_bags('day7/input.txt')
    for color in bags:
        if is_valid(bags, color):
            cnt += 1
    print(cnt - 1)


def part2():
    bags = parse_bags('day7/input.txt')
    print(sum_bags(bags, 'shiny gold') - 1)


part1()
part2()
