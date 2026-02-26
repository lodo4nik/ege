from functools import lru_cache

def f(n):
    if n <= 1:
        return 1
    else:
        return (n+1) * f(n-1)

for n in range(220, 4, -1): f(n)

print(f(200)/f(198))
