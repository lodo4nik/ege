REPEAT = 5 # x
R = 4 # vars
from itertools import product, permutations

def f1(x, y, z, w):
    return (x and (not y)) or (y == z) or (not w)

for x1, x2, x3, x4, x5 in product([0, 1], repeat=REPEAT):
    t = (
        (0, x1, x2, 0, 0),
        (0, 1, 0, 1, 0),
        (x3, 1, 0, x4, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f1(**dict(zip(p, line))) == line[-1] for line in t):
                print(*p)