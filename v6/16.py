from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 110000:
        return 4 + n
    else:
        return (n+7) * f(n+12)

for n in range(110000, 130, -1): f(n)

res = (f(113) + f(137)) / (2 * f(149))
print(res)
