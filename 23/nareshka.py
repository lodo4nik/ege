def f(x, end):
    if x > end: return 0
    if x == end: return 1
    return f(x+1, end) + f(x+2, end) + f(x*3, end)

a = f(6, 15)*f(15, 25)
b = f(6, 21)*f(21, 25)
c = f(6, 15)*f(15,21)*f(21, 25)

print(a+b-c)