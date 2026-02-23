def f(x, end):
    if x < end: return 0
    if x == end: return 1
    return f(x-5, end) + f(x-9, end) + f(x//2, end)

print(f(97, 13))
