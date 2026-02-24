from math import *

for lent in range(1, 10000):
    w = ceil((lent * ceil(log(1987+52+10, 2))/8))
    if w * 3000 <= 754*1024:
        print(lent)
