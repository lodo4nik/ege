def f(x, end):
    if x > end or x == 20: return 0
    if x == end: return 1
    return f(x+3, end) + f(x*2, end) + f(x**2, end)
# программ, содержащих число 12 не существует
print(f(2, 128))
