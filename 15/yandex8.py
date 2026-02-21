# https://education.yandex.ru/ege/inf/task/270eff1c-fe8a-44ab-8390-a9d6e638ae0f

P = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
Q = {4, 9, 14, 19, 24, 29, 34, 39, 44, 49}
A = set(range(-1000, 1000))

for x in range(-1000, 1000):
    f = ((x in A) <= (x in P)) or ((x not in Q) <= (x not in A))
    if f == 0:
        A.remove(x)
            
print(sum(A))
