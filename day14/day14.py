from bitarray import bitarray, util
import itertools


def part1():
    or_mask = None
    and_mask = None

    memory = {}

    f = open('day14/input.txt')

    lines = list(f.readlines())

    for line in lines:
        words = line.strip().split(" = ")
        if words[0] == 'mask':
            or_mask = bitarray(words[1].replace('X', '0'))
            and_mask = bitarray(words[1].replace('X', '1'))
        else:
            address = int(words[0].replace('mem[', "").replace(']', ''))
            val = util.int2ba(int(words[1]), length=36)
            memory[address] = (val & and_mask) | or_mask

    sum = 0
    for addr in memory:
        sum += util.ba2int(memory[addr])
    print('part 1:', sum)


def part2():

    memory = {}
    mask = None

    for line in list(open('day14/input.txt').readlines()):
        words = line.strip().split(" = ")
        if words[0] == 'mask':
            mask = words[1].strip()
        else:
            address = int(words[0].replace('mem[', "").replace(']', ''))
            val = util.int2ba(address, length=36)
            s = list(val.to01())
            num_x = 0
            for i, c in enumerate(mask):
                if c == '1':
                    s[i] = '1'
                elif c == 'X':
                    s[i] = 'X'
                    num_x += 1
            s = "".join(s)
            for c in itertools.product('01', repeat=num_x):
                new_addr = s
                for c1 in c:
                    new_addr = new_addr.replace("X", c1, 1)
                memory[util.ba2int(bitarray(new_addr))] = int(words[1].strip())

    sum = 0
    for addr in memory:
        sum += memory[addr]

    print('part 2:', sum)


part1()
part2()
