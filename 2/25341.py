from itertools import product, permutations

from pandas.io.formats.format import return_docstring


def f(x, y, z, w):
    return (w == z) or (not (y <= w)) or (not x)

for x1, x2, x3, x4, x5 in product([0,1], repeat=5):
    t = (
        (x1, 0, 1, 0, 0),
        (x2, 1, 1, x3, 0),
        (0, x4, x5, 0, 0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in t):
                print(p)