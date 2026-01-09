from functools import lru_cache

@lru_cache(None)
def g(n):
    if n >= 264685:
        return int(n / 20 + 33)
    if n < 264685:
        return g(n+9)-2

def f(n):
    if n >= 21:
        return f(n-5) + 3480
    if n < 21:
        return 10 * (g(n-9) - 30)

for n in range(264685, 675, -1): g(n)

print(g(264685))