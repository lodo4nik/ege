from itertools import product, permutations

def f(z, x, y, w):
    return z or (x == (y <= w))

for x1, x2, x3, x4 in product([0,1], repeat=4):
    t = (
        (1, 0, 1, x1, 0),
        (1, 0, x2, 1, 0),
        (x3, x4, 1, 0, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations("xywz", 4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(''.join(p))