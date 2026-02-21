# https://education.yandex.ru/ege/inf/task/25343130-15c0-4096-a396-4a72c38efffe

P = range(12, 63)
Q = range(52, 93)

def f(x, P, Q, A):
    return (not((not(x in A)) and (x in P))) or (x in Q)

for end_a in range(11, 1000):
    A = range(10, end_a+1)
    if all(f(x, P, Q, A) == True for x in range(1, 1000)):
        print(A)
        break
