# https://education.yandex.ru/ege/inf/task/dc4c312e-1acd-406e-83a6-d4aac88cf80e

from math import *

def findsum(n):
    sums = []
    for i in range(1, n//2+1):
        if n % i == 0:
            sums.append(i)
    if len(sums) == 1:
        return 0
    return sums[1] + sums[-1]

for n in range(800000, 900000):
    m = findsum(n)
    if m % 10 == 4:
        print(n, m)