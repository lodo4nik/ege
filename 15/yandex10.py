# https://education.yandex.ru/ege/inf/task/602f4f53-56d1-4333-8b72-07f5cf6c7f65

A = range(5, 18)
B = range(10, 22)
C = range(12, 31)


for x in (30, 9, 4):
    if (not(x in B)) and (not(x in A)) or (x in C):
        print(1)
    else:
        print(0)
