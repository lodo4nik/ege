from functools import lru_cache

@lru_cache(None)
def f(n):
    if n == 1:
        return 2
    if n >= 2:
        return 3*f(n-1)-n

for n in range(1, 2026): f(n)

print((f(2025)-f(2023)-1)/3**2022)
