from itertools import product, permutations
def f1(x, y, z, w):
    return (w == x) and (y <= z)

def f2(x, y, z, w):
    return (w <= x) <= (y == z)

for x1, x2, x3, x4, x5 in product([0,1], repeat=5):
    t = (
        (1, x1, 1, 1, 1, 0),
        (x2, 1, 0, 0, 1, x3),
        (x4, 0, 0, x5, 0, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f1(**dict(zip(p, line))) == line[-2] for line in t):
                if all(f2(**dict(zip(p, line))) == line[-1] for line in t):
                    print(*p)