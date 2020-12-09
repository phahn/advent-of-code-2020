def parse():
    f = open('day8/input.txt')

    program = []
    for line in f.readlines():
        tokens = line.split(" ")
        program.append((tokens[0], int(tokens[1].strip())))
    # print(program)
    return program


def run(program):
    visited = set()
    visited.add(0)
    ip = 0
    pip = 0
    acc = 0
    while ip < len(program):
        (ins, val) = program[ip]
        pip = ip
        if ins == "acc":
            acc += val
            ip += 1
        elif ins == 'jmp':
            ip += val
        elif ins == 'nop':
            ip += 1

        if ip in visited:
            print('visited twice: ', acc, ip, pip)
            return -1
        else:
            visited.add(ip)
    return acc


def part1():
    program = parse()
    run(program)


def part2():
    program = parse()
    for i in range(len(program)):

        p = parse()
        (ins, val) = p[i]
        if ins == 'nop':
            p[i] = ('jmp', val)
        elif ins == 'jmp':
            p[i] = ('nop', val)

        r = run(p)
        if r > -1:
            print('change line ', i, r)


part1()
# part2()
