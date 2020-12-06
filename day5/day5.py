def get_seat_id_optimized(inp):
    # convert to binary
    seat_row = int(inp[:7].replace('F', '0').replace('B', '1'), 2)
    seat_col = int(inp[7:].replace('L', '0').replace('R', '1'), 2)
    return seat_row * 8 + seat_col


def get_seat_id(inp):
    rows = inp[:7]
    cols = inp[7:]

    (start, end) = (0, 127)
    for r in rows:
        if r == 'F':
            (start, end) = (start, (start + end) // 2)
        else:
            (start, end) = ((start + end) // 2 + 1, end)

    seat_row = start

    (start, end) = (0, 7)
    for r in cols:
        if r == 'L':
            (start, end) = (start, (start + end) // 2)
        else:
            (start, end) = ((start + end) // 2 + 1, end)

    seat_col = start

    return seat_row * 8 + seat_col


def part1():
    f = open('day5/input.txt')
    max_id = max(get_seat_id_optimized(line.strip()) for line in f.readlines())
    print(max_id)


def part2():
    f = open('day5/input.txt')
    ids = list(
        get_seat_id_optimized(line.strip()) for line in f.readlines())
    missing_ids = list(id for id in range(min(ids), max(ids)) if id not in ids)
    print(missing_ids)

# print(get_seat_id('FBFBBFFRLR'))
# print(get_seat_id('BFFFBBFRRR'))
# print(get_seat_id('FFFBBBFRRR'))
# print(get_seat_id('BBFFBBFRLL'))


part1()
part2()
