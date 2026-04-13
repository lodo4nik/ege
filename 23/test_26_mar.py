def f(x, end):
    if x > end or x == 10: return 0
    if x == end: return 1
    return f(x+2, end)+f(x+4, end)+f(x*2, end)

print(f(2, 16))
