from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n+3+f(n+3)

for i in range(23, 2025): f(i)

print(f(23)-f(21))