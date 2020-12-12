def parse_commands():
    f = open('day12/input.txt')
    commands = []
    for line in f.readlines():
        c = line[0]
        v = int(line[1:])
        commands.append((c, v))
    return commands


def add(p, v):
    return (p[0] + v[0], p[1] + v[1])


def mul(v, l):
    return (v[0] * l, v[1] * l)


def rotate(v, a):
    a = a % 360
    if a == 0:
        return v
    if a == 90:
        return (-v[1], v[0])
    if a == 180:
        return (-v[0], -v[1])
    if a == 270:
        return (v[1], -v[0])
    return None


def part1():
    commands = parse_commands()

    direction = (1, 0)
    position = (0, 0)

    for cmd in commands:
        if cmd[0] == "F":
            position = add(position, mul(direction, cmd[1]))
        elif cmd[0] == "N":
            position = add(position, mul((0, -1), cmd[1]))
        elif cmd[0] == "S":
            position = add(position, mul((0, 1), cmd[1]))
        elif cmd[0] == "E":
            position = add(position, mul((1, 0), cmd[1]))
        elif cmd[0] == "W":
            position = add(position, mul((-1, 0), cmd[1]))
        elif cmd[0] == "R":
            direction = rotate(direction, cmd[1])
        elif cmd[0] == "L":
            direction = rotate(direction, 360 - cmd[1])

    distance = abs(position[0]) + abs(position[1])
    print(distance)


def sub(p, v):
    return (v[0] - p[0], v[1] - p[1])


def part2():
    commands = parse_commands()

    p = (0, 0)
    w = (10, -1)

    for cmd in commands:
        if cmd[0] == "F":
            p = add(p, mul(w, cmd[1]))
        elif cmd[0] == "N":
            w = add(w, mul((0, -1), cmd[1]))
        elif cmd[0] == "S":
            w = add(w, mul((0, 1), cmd[1]))
        elif cmd[0] == "E":
            w = add(w, mul((1, 0), cmd[1]))
        elif cmd[0] == "W":
            w = add(w, mul((-1, 0), cmd[1]))
        elif cmd[0] == "R":
            w = rotate(w, cmd[1])
        elif cmd[0] == "L":
            w = rotate(w, 360 - cmd[1])

    distance = abs(p[0]) + abs(p[1])
    print(distance)


part1()
part2()
