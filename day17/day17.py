from itertools import product


def parse():
    f = open('day17/input.txt')

    active = set()

    lines = [l.strip() for l in f.readlines()]
    # print(lines)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                active.add((x, y, 0))

    w = len(lines[0])
    h = len(lines)
    d = 1
    t = 1

    return ((w, h, d, t), active)


def parse2():
    f = open('day17/input.txt')

    active = set()

    lines = [l.strip() for l in f.readlines()]
    # print(lines)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                active.add((x, y, 0, 0))

    w = len(lines[0])
    h = len(lines)
    d = 1
    t = 1

    return ((w, h, d, t), active)


# print(active, w, h)


def active_neighbours(c, active):
    x, y, z = c
    count = 0
    for n in product([-1, 0, 1], repeat=3):
        if n != (0, 0, 0):
            tx = x+n[0]
            ty = y+n[1]
            tz = z+n[2]
            if (tx, ty, tz) in active:
                count += 1
    return count


def active_neighbours2(c, active):
    x, y, z, w = c
    count = 0
    for n in product([-1, 0, 1], repeat=4):
        if n != (0, 0, 0, 0):
            tx = x + n[0]
            ty = y + n[1]
            tz = z + n[2]
            tw = w + n[3]
            if (tx, ty, tz, tw) in active:
                count += 1
    return count


def print_cubes(cycle, w, h, d, active):
    for z in range(-cycle, d + cycle):
        print('z = ', z)
        for y in range(-cycle, h + cycle):
            for x in range(-cycle, w + cycle):
                c = (x, y, z)
                if c in active:
                    print('#', end='')
                else:
                    print('.', end='')
            print('')


def part1():
    cycle = 0

    ((w, h, d, _), active) = parse()

    # print_cubes(0, w, h, d, active)
    print(0, len(active))

    # 6 cycles
    for _ in range(0, 6):

        new_active = set(active)
        cycle += 1

        for x in range(-cycle, w + cycle):
            for y in range(-cycle, h + cycle):
                for z in range(-cycle, d + cycle):
                    c = (x, y, z)
                    n = active_neighbours((x, y, z), active)
                    # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
                    if c in active:
                        if n not in (2, 3):
                            new_active.remove(c)
                    # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
                    else:
                        if n == 3:
                            new_active.add(c)

        active = new_active

        # print_cubes(cycle, w, h, d, active)
        print(cycle, len(active))


def part2():
    cycle = 0

    ((width, h, d, t), active) = parse2()

    # print_cubes(0, w, h, d, active)
    print(0, len(active))

    # 6 cycles
    for _ in range(0, 6):

        new_active = set(active)
        cycle += 1

        for x in range(-cycle, width + cycle):
            for y in range(-cycle, h + cycle):
                for z in range(-cycle, d + cycle):
                    for w in range(-cycle, t + cycle):
                        c = (x, y, z, w)
                        n = active_neighbours2(c, active)
                        # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
                        if c in active:
                            if n not in (2, 3):
                                new_active.remove(c)
                        # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
                        else:
                            if n == 3:
                                new_active.add(c)

        active = new_active

        # print_cubes(cycle, w, h, d, active)
        print(cycle, len(active))


part1()
part2()
