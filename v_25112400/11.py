from math import *

for lenth in range(1, 100000):
    word = ceil(lenth * ceil(log(10 + 52 + 454, 2)) / 8)
    if 31_922 * word > 2*1024*1024*1024:
        print(lenth)
        exit()