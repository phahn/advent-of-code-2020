from copy import deepcopy
from collections import deque
from itertools import product


def parse_map():
    f = open('day11/input.txt')

    m = []
    for line in f.readlines():
        m.append([c for c in line.strip()])
    return m


def sum_seats(p, x, y, f):
    o = 0
    for vx, vy in product([-1, 0, 1], repeat=2):
        if vx == 0 and vy == 0:
            continue
        o += f(p, x, y, vx, vy)
    return o


def count_part1(m, x, y, vx, vy):
    w = len(m[0])
    h = len(m)

    px = x + vx
    py = y + vy

    if px >= 0 and px < w and py >= 0 and py < h and m[py][px] == '#':
        return 1
    return 0


def count_part2(m, x, y, vy, vx):
    w = len(m[0])
    h = len(m)

    px = x
    py = y

    while True:
        px += vx
        py += vy

        if not(px >= 0 and px < w and py >= 0 and py < h):
            return 0
        elif m[py][px] == "#":
            return 1
        elif m[py][px] == "L":
            return 0
    return 0


def print_map(m):
    WIDTH = len(m[0])
    HEIGHT = len(m)
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            print(m[y][x], end='')
        print()


def count_seats(m):
    WIDTH = len(m[0])
    HEIGHT = len(m)
    s = 0
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            if m[y][x] == "#":
                s += 1
    return s


def day11(thr, f):
    m = parse_map()
    # print_map(m)
    WIDTH = len(m[0])
    HEIGHT = len(m)

    change = True

    while change:
        change = False
        # print(results)
        p = deepcopy(m)
        for y in range(0, HEIGHT):
            for x in range(0, WIDTH):

                s = m[y][x]
                o = sum_seats(p, x, y, f)

                if s == 'L' and o == 0:
                    m[y][x] = "#"
                    change = True
                if s == '#' and o >= thr:
                    m[y][x] = "L"
                    change = True

    return count_seats(m)


print('part 1:', day11(4, count_part1))
print('part 2:', day11(5, count_part2))
