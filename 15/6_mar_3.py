P = range(23, 45)
Q = range(34, 57)

A = [x for x in range(-100, 100)]

for x in range(-100, 100):
    f = (x not in A) or (x not in P) and (x in Q)

    if f == 0:
        A.remove(x)        

print(A)
