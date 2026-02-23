from math import *

for n in range(1, 100000):
    w = ceil(96*ceil(log(n, 2))/8)
    if w * 50000 >= 6*1024*1024:
        print(n)
