# https://education.yandex.ru/ege/inf/task/d382d953-d360-46eb-96c8-295f3b5c63fb

import sys
sys.setrecursionlimit(10000)

def f(n):
    if n >= 2222:
        return n
    else:
        return n**3 + f(n+2)

print(f(4)-f(10))