# https://education.yandex.ru/ege/inf/task/8e383cd1-86c7-4ddb-8e69-af16360eb883

P = range(117, 159)
Q = range(129, 181)
A = set()

for x in range(-1000, 1000):
    f = (x in P) <= (((x in Q) and (not(x in A))) <= (not(x in P)))
    if f == 0:
        A.add(x)
print(len(A)-1)
