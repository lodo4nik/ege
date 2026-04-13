from math import *
for N in range(1, 1000):
    word = ceil(197*ceil(log(N, 2))/8)
    if 178_080*word > 25*1024*1024:
        print(N)
        break
