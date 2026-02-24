def f(x, end, deny=9):
    if x < end or x == deny: return 0
    if x == end: return 1
    return f(x-1, end, deny) + f(x-3, end, deny) + f(x//3, end, deny)

print(f(21, 12) * f(12, 3))
