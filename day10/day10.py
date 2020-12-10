def part1():
    f = open('day10/input.txt')
    adapters = sorted([int(line) for line in f.readlines()])

    r = {1: 0, 2: 0, 3: 1}
    s = 0
    for adapter in adapters:
        diff = adapter - s
        r[diff] += 1
        s += diff
    print('part 1: ', r[1] * r[3])


def part2():
    f = open('day10/input.txt')
    adapters = sorted([int(line) for line in f.readlines()])

    c = {
        0: 1
    }

    for adapter in adapters:
        c[adapter] = 0
        for diff in range(1, 4):
            if (adapter - diff) in c:
                c[adapter] += c[adapter-diff]
    print('part 2: ', c[adapters[len(adapters) - 1]])


part1()
part2()
