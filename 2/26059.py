from itertools import product, permutations

def f(x, y, w, z):
    return w and ((y and z) or (not((not x) <= y)))

for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
    t = (
        (x1, x2, 0, x3, 1),
        (0, x4, 1, 1, 1),
        (1, 0, x5, 1, 1)
    )
    if len(t) == len(set(t)):
        for p in permutations("xyzw", r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(p)

