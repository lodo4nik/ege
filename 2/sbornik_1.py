from itertools import permutations, product

def f(x, y, z, w):
    return x <= (not ((y <= z) and (z == (not w))))

for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        (0, x1, x2, 0, 0),
        (x3, 1, 1, x4, 0),
        (x5, 1, 0, 0, 0)
    )
    if len(t)==len(set(t)):
        for p in permutations("xyzw", r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)
