def day15(start, stop):
    prev = {}
    last = None
    for r in range(1, stop + 1):
        if r < len(start) + 1:
            n = start[r - 1]
        else:
            if last in prev:
                n = (r - 1) - prev[last]
            else:
                n = 0
        prev[last] = r - 1
        last = n
    print(n)


day15([0, 3, 6], 2020)
day15([1, 3, 2], 2020)
day15([2, 1, 3], 2020)
day15([1, 2, 3], 2020)
day15([2, 3, 1], 2020)
day15([3, 2, 1], 2020)
day15([3, 1, 2], 2020)
day15([0, 20, 7, 16, 1, 18, 15], 2020)

day15([0, 3, 6], 30000000)
day15([0, 20, 7, 16, 1, 18, 15], 30000000)
