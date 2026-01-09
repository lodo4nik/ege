def f(x, end):
    if x > end: return 0
    if x == end: return 1
    else: return f(x+1, end) + f(x*2, end)

print(f(3, 6)*f(6, 12)*f(12, 16))