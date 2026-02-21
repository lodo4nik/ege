# https://education.yandex.ru/ege/inf/task/ad49b4d3-62dc-420f-aa97-519d891a80f5

P = range(20, 68)
Q = range(33, 99)
A = set()

for x in range(-1000, 1000):
    f = (x in P) <= (((x in Q) and (not(x in A))) <= (not(x in P)))
    if f == 0:
        A.add(x)
        
print(len(A)-1)
