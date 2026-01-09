# n?
from math import *

for n in range(1, 10000):
    word = ceil(246 * ceil(log(n, 2)) / 8)
    if 703_569*word < 77*1024*1024:
        print(n)