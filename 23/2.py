# https://education.yandex.ru/ege/inf/task/a21521c7-2b20-4e05-acde-e6fb294c94f8

def f(x, end):
    if x > end or x == 10: return 0
    if x == end: return 1
    return f(x+1, end)+f(x*2, end)

print(f(1, 30))
