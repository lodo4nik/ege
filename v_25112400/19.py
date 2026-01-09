def f(s, m):
    if s >= 444: return m % 2 == 0
    if m == 0: return 0
    h = [f(s+2, m-1), f(s+5, m-1), f(s*3, m-1)]
    return any(h) if m % 2 != 0 else all(h)

print([s for s in range(1, 401) if f(s, 2)])
print([s for s in range(1, 401) if not f(s, 1) and f(s, 3)])
print([s for s in range(1, 401) if not f(s, 2) and f(s, 4)])