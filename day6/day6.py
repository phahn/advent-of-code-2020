def read_groups(file):
    f = open(file)
    groups = []
    group = []
    for line in f.readlines():
        if line == '\n':
            groups.append(group)
            group = []
        else:
            group.append(set(line.strip()))

    groups.append(group)
    return groups


def part1():
    sum = 0
    for group in read_groups('day6/input.txt'):
        sum += len(set.union(*[s for s in group]))
    print(sum)


def part2():
    sum = 0
    for group in read_groups('day6/input.txt'):
        sum += len(set.intersection(*[s for s in group]))
    print(sum)


part1()
part2()
