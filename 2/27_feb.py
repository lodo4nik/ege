from itertools import product, permutations

def f(x, y, w, z):
    return w and (y == (z <= (x or y)))

for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        (x1, 0, 0, x2, 1),
        (1, x3, 1, 0, 1),
        (x4, x5, 1, 0, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations("xyzw", r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(p)
