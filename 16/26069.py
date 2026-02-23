from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 30:
        return f(n-5)+210
    if n < 30:
        return 3 * (g(n+4) - 12)

@lru_cache(None)
def g(n):
    if n >= 120:
        return 2 * h(n-10)+5
    if n < 120:
        return g(n+6) - 4

@lru_cache(None)
def h(n):
    if n >= 5000:
        return int(n/25) + 7
    if n < 5000:
        return h(n+2) + 3

for n in range(5000, 256, -1): h(n)

print(f(257))
