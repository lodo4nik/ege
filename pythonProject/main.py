from functools import lru_cache


@lru_cache(None)
def f(a):
    if a >= 37:
        return 0
    t = [f(a + 2), f(a * 2)]
    n = [i for i in t if i <= 0]
    if n:
        return -max(n) + 1
    else:
        return -max(t)


for i in range(1, 165):
    if f(i) == -1:
        print('19:', i)
    if f(i) == 2:
        print('20:', i)
    if f(i) == -2:
        print('21:', i)
