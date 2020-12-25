b = 7
e = 1
m = 20201227

public_keys = [14205034, 18047856]

#  find e by trying all possibilities
while pow(b, e, m) not in public_keys:
    e += 1

if pow(b, e, m) == public_keys[0]:
    print('part 1:', pow(public_keys[1], e, m))
else:
    print('part 1:', pow(public_keys[0], e, m))
