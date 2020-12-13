
def part1():
    f = open('day13/input.txt')
    lines = list(f.readlines())
    time = int(lines[0])
    busses = []
    for bus in lines[1].split(","):
        if bus == 'x':
            continue
        else:
            busses.append(int(bus))

    m = max(busses)

    for i in range(time, time + m):
        for bus in busses:
            if i % bus == 0:
                print((i - time) * bus)
                return


def part2():
    f = open('day13/input.txt')
    lines = list(f.readlines())
    n = []
    a = []
    N = 1
    for i, bus in enumerate(lines[1].split(",")):
        if bus == 'x':
            continue
        else:
            n.append(int(bus))
            a.append((int(bus) - i) % int(bus))

    y = []

    for i in range(0, len(n)):
        N *= n[i]

    for i in range(0, len(n)):
        y.append(N // n[i])

    z = []
    for i in range(0, len(n)):
        z.append(pow(y[i], -1, n[i]))

    x = 0
    for i in range(0, len(n)):
        x += a[i] * y[i] * z[i]

    print(x % N)


part1()
part2()
