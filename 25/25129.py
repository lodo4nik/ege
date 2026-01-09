from math import *
def f(x):
    for i in range(222, x+1, 222):
        if len([j for j in str(i) if int(j) % 2 != 0]) == 0:
            if log((x-i), 5) == int(log((x-i), 5)):
                return int(log((x-i), 5))
    return -1

k = 0
for i in range(1_000_001, 1_200_000):
    if k != 5:
        if f(i) != -1:
            print(i, f(i))
            k+=1
    else: exit()