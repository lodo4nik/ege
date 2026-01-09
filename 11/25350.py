from math import *

for n in range(1, 1000):
    word = ceil(105*ceil(log(n, 2)) / 8)
    if word*65_536 >= 7*1024*1024:
        print(n)
        break