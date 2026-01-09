from functools import lru_cache

@lru_cache(None)
def g(n):
    if n >= 30000:
        return 3
    if n < 30000:
        return g(n+3) + 7
@lru_cache(None)
def f(n):
    return g(n+1)

for i in range(30000, 1, -1): g(i)

print(f(1500))