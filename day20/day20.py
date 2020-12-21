from copy import deepcopy
from math import sqrt

f = open('day20/input.txt')

tiles = f.read().split('\n\n')

T = {}


def rotate90(original):
    orig = deepcopy(original)
    return list(zip(*orig[::-1]))


def flipH(original):
    return list(original[::-1])


def get_tile(B, tile, r, f):
    t = deepcopy(B[tile])

    if r == 0:
        t = t
    elif r == 90:
        t = rotate90(t)
    elif r == 180:
        t = rotate90(rotate90(t))
    elif r == 270:
        t = rotate90(rotate90(rotate90(t)))

    if f == 1:
        t = flipH(t)
    return t


def get_borders(B, tile, r, f):

    t = get_tile(B, tile, r, f)

    borders = []
    top = "".join(t[0])
    bottom = "".join(t[len(t) - 1])
    left = "".join([t[i][0] for i in range(len(t))])
    right = "".join([t[i][len(t[0]) - 1] for i in range(len(t))])

    borders.append(left)
    borders.append(top)
    borders.append(right)
    borders.append(bottom)

    return borders


for tile in tiles:
    id = None
    for line in tile.split('\n'):
        if line.startswith("Tile"):
            id = int(line.split(" ")[1][:-1])
            T[id] = []
        else:
            T[id].append(list(line))


def print_tile(t):
    for y in range(0, len(t)):
        for x in range(0, len(t[0])):
            print(t[y][x], end="")
        print("\n", end="")


B = {}

LT = {}
TP = {}
RT = {}
BM = {}

for tile in T:
    for r in (0, 90, 180, 270):
        for f in (0, 1):
            borders = get_borders(T, tile, r, f)
            if borders[0] in LT:
                LT[borders[0]].append((tile, r, f))
            else:
                LT[borders[0]] = [(tile, r, f)]

            if borders[1] in TP:
                TP[borders[1]].append((tile, r, f))
            else:
                TP[borders[1]] = [(tile, r, f)]

            if borders[2] in RT:
                RT[borders[2]].append((tile, r, f))
            else:
                RT[borders[2]] = [(tile, r, f)]

            if borders[3] in BM:
                BM[borders[3]].append((tile, r, f))
            else:
                BM[borders[3]] = [(tile, r, f)]
            B[(tile, r, f)] = borders


def without_tile(C, t):
    C2 = {}
    for c in C:
        for v in C[c]:
            if v[0] != t:
                if c not in C2:
                    C2[c] = [v]
                else:
                    C2[c].append(v)
    return C2


CORNER = []
P1 = set()

for tile in B:

    borders = B[tile]

    if borders[0] not in without_tile(RT, tile[0]) and borders[1] not in without_tile(BM, tile[0]) and borders[2] in without_tile(LT, tile[0]) and borders[3] in without_tile(TP, tile[0]):
        CORNER.append(tile)
        P1.add(tile[0])

p1 = 1
for x in P1:
    p1 *= x

print('part 1:', p1)

R = int(sqrt(len(T)))
C = int(sqrt(len(T)))

for corner in CORNER:

    G = [[None for _ in range(C)] for _ in range(R)]

    G[0][0] = corner

    def bottom_border(t):
        return B[t][3]

    def right_border(t):
        return B[t][2]

    def find_tile(used, left, top, o1, o2):
        for t in B:
            if t[0] not in used and t not in [o1, o2] and (left is None or B[t][0] == left) and (top is None or B[t][1] == top):
                return t
        return None

    USED = set()
    USED.add(corner[0])

    for r in range(R):
        for c in range(C):

            if G[r][c]:
                continue

            if c-1 < 0:
                tile = find_tile(USED, None, bottom_border(
                    G[r - 1][c]), G[r-1][c], None)
            elif r - 1 < 0:
                tile = find_tile(USED, right_border(
                    G[r][c - 1]), None, G[r][c-1], None)
            else:
                tile = find_tile(USED, right_border(
                    G[r][c - 1]), bottom_border(G[r - 1][c]), G[r-1][c], G[r][c-1])

            G[r][c] = tile
            USED.add(tile[0])

    img = [['?' for x in range(R * 8)] for _ in range(C * 8)]
    for r in range(R):
        for c in range(C):
            t, rot, f = G[r][c]
            tile = get_tile(T, t, rot, f)
            for rr in range(8):
                for cc in range(8):
                    img[r*8+rr][c*8+cc] = tile[rr + 1][cc + 1]

    MONSTER = [
        list('                  # '),
        list('#    ##    ##    ###'),
        list(' #  #  #  #  #  #   ')]

    m = 0

    for r in range(R * 8 - len(MONSTER)):
        for c in range(R * 8 - len(MONSTER[0])):

            count = 0
            match = True
            for rr in range(len(MONSTER)):
                for cc in range(len(MONSTER[0])):
                    if MONSTER[rr][cc] == " ":
                        continue
                    if MONSTER[rr][cc] == "#" and img[r + rr][c + cc] == "#":
                        continue
                    else:
                        match = False
            if match:
                m += 1

    s = 0
    for r in range(R * 8):
        for c in range(R * 8):
            if img[r][c] == "#":
                s += 1
    if m > 0:
        print("part 2:", s - m * 15)
