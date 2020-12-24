f = open('day24/input.txt')


def add(pos, off):
    return (pos[0] + off[0], pos[1] + off[1], pos[2] + off[2])


def find_all_neighbours(pos):
    a = []
    for d in ['e', 'se', 'sw', 'w', 'nw', 'ne']:
        a.append(find_neighbour(pos, d))
    return a


def find_neighbour(pos, d):
    D = {
        'e': (+1, -1, 0),
        'se': (+1, 0, -1),
        'sw': (0, +1, -1),
        'w': (-1, +1, 0),
        'nw': (-1, 0, +1),
        'ne': (0, -1, +1),
    }
    return add(pos, D[d])


instr = []
for line in f.readlines():
    directions = []
    direction = None
    for c in line:
        if c == "w":
            if direction == None:
                directions.append("w")
            elif direction == "n":
                directions.append("nw")
            elif direction == 's':
                directions.append("sw")
            direction = None
        if c == 'e':
            if direction == None:
                directions.append("e")
            elif direction == "n":
                directions.append("ne")
            elif direction == 's':
                directions.append("se")
            direction = None
        if c == 's':
            if direction == None:
                direction = 's'
        if c == 'n':
            if direction == None:
                direction = 'n'
    instr.append(directions)

FLIPPED = set()

for d in instr:
    pos = (0, 0, 0)
    for dd in d:
        pos = find_neighbour(pos, dd)
    # tile has been flipped
    if pos in FLIPPED:
        FLIPPED.remove(pos)
    else:
        FLIPPED.add(pos)

print('part 1:', len(FLIPPED))

#  part 2

for day in range(0, 100):
    to_check = set()
    #  we only need to check black tiles and its neighbours
    for p in FLIPPED:
        to_check.add(p)
        for n in find_all_neighbours(p):
            to_check.add(n)

    # print(len(to_check))

    TEMP = set()
    for p in to_check:
        count = 0
        for n in find_all_neighbours(p):
            if n in FLIPPED:
                count += 1
        if p in FLIPPED:
            if not (count == 0 or count > 2):
                TEMP.add(p)
        if p not in FLIPPED and count == 2:
            TEMP.add(p)
    FLIPPED = TEMP
    print(day + 1, len(FLIPPED))
