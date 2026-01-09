from math import *

def f(x):
    divs = []
    for d in range(2, int(sqrt(x))+1):
        if x % d == 0 and d != 11:
            divs.append(d)
            divs.append(x // d)
    return divs

k = 0
for i in range(1_350_051, 1_360_051):
    eleven_divs = [i for i in f(i) if str(i).endswith("11")]
    if eleven_divs and k != 5:
        print(i, min(eleven_divs))
        k += 1