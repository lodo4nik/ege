from functools import lru_cache

@lru_cache(None)
def g(n):
    if n >= 248045:
        return n / 20 + 28
    if n < 248045:
        return g(n+9)-4

def f(n):
    if n >= 19:
        return f(n-4)+3580
    if n < 19:
        return 6 * (g(n-7) - 36)

for n in range(248045, 673, -1): g(n)

print(f(673))