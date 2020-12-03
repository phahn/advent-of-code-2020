
def load_map(file):
    f = open(file)
    map = []
    for line in f.readlines():
        map.append(list(line.strip()))
    return map


def part1(slope):
    trees = 0
    m = load_map('day3/input.txt')
    coord = (0 + slope[0], 0 + slope[1])
    while coord[0] < len(m):

        if m[coord[0]][coord[1] % len(m[0])] == '#':
            trees += 1
        coord = (coord[0] + slope[0], coord[1] + slope[1])

    return(trees)


print(part1((1, 3)))
print(part1((1, 1)) * part1((1, 3)) * part1((1, 5))
      * part1((1, 7)) * part1((2, 1)))
