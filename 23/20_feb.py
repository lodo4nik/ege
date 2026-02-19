def f(x, end, deny):
    if x > end or x == deny: return 0
    if x == end: return 1
    return f(x+1, end, deny) + f(x+2, end, deny) + f(x*3, end, deny)

print(f(4, 10, 20)*f(10, 22, 20))