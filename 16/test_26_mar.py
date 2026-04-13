from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 2 == 0:
        return n + f(n-1)
    if n > 2 and n % 2 != 0:
        return f(n-3)

for n in range(1, 2026): f(n)

print(f(2026)-f(2016))
