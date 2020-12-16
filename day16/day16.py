f = open('day16/input.txt')

blocks = f.read().split('\n\n')

rules = {}

# rules
for line in blocks[0].split('\n'):
    (field, ranges) = line.split(":")
    rules[field] = []
    for r in ranges.split(" or "):
        (rmin, rmax) = r.split("-")
        rules[field].append((int(rmin), int(rmax) + 1))

# my passport
my_passport = [int(x) for x in blocks[1].split('\n')[1].split(',')]

# other passports
passports = []
for l in blocks[2].split('\n')[1:]:
    passports.append([int(x) for x in l.split(',')])

valid_passports = []
error_rate = 0
for p in passports:
    valid = True
    for v in p:
        if not any(f for f in rules if (v in range(*rules[f][0]) or v in range(*rules[f][1]))):
            error_rate += v
            valid = False
    if valid:
        valid_passports.append(p)

print('part 1:', error_rate)


# part 2:

index = {}

for f in rules.keys():
    index[f] = []
    for r in range(0, len(valid_passports[0])):
        invalid = False
        for p in valid_passports:
            if not(p[r] in range(*rules[f][0]) or p[r] in range(*rules[f][1])):
                invalid = True
                break
        if not invalid:
            index[f].append(r)

solved = set()

while True:
    val = [i for i in index.values() if len(i) == 1 and i[0] not in solved]
    if val:
        val = val[0]
    else:
        break
    solved.add(val[0])
    for v in index.values():
        if len(v) > 1 and val[0] in v:
            v.remove(val[0])

p_sum = 1
for f in index.keys():
    if f.startswith("departure"):
        p_sum *= my_passport[index[f][0]]

print('part 2', p_sum)
