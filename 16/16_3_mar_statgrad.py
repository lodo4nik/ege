from functools import lru_cache

@lru_cache(None)
def f(n):
    if n > 19999:
        return n + f(n-6)
    if n < 20000:
        return n + g(n-3)
    
@lru_cache(None)
def g(n):
    if n < 20000:
        return 20 + n + g(n+4)
    if n > 19999:
        return n**2

for n in range(20000, 65000): g(n); f(n)

print(f(65000))
