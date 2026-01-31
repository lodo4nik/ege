from math import *

def find_divs(x):
    divs = []
    for div in range(1, int(sqrt(x)+1)):
        if x % div == 0:
            divs.append(div)
            divs.append(x//div)
    if len(divs) == len(set(divs)) and len(divs) == 4:
        return sorted(divs)

for n in range(700_000, 800_000):
    d = find_divs(n)
    if d != None:
        if d[-2] - d[1] <= 15:
            print(n, d[-2] - d[1])