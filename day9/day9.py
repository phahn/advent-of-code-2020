def part1(f, p):
    f = open(f)
    n = [int(l) for l in f.readlines()]

    for i in range(p, len(n)):
        s = set()
        for j in range(i-p, i):
            for k in range(j + 1, i):
                s.add(n[j] + n[k])
        if n[i] not in s:
            print(n[i])
            break


def part2(f, r):
    f = open(f)
    n = [int(l) for l in f.readlines()]

    for i in range(0, len(n)):
        s = n[i]
        for j in range(i + 1, len(n)):
            s += n[j]
            if r == s:
                print(min(n[i:j]) + max(n[i:j]))
                return
            if s > r:
                break


# examples
part1('day9/example.txt', 5)
part2('day9/example.txt', 127)

# input
part1('day9/input.txt', 25)
part2('day9/input.txt', 3199139634)
