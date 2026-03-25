from math import *

stepens = [3**i for i in range(1, 17)]

def f(x):
    raznosts = [x-i for i in stepens]
    uslovie = [i for i in raznosts if i%2!=0 and i%103==0 and i>0]
    return uslovie
        
k = 0
for x in range(100000, 999999+1):
    if k < 5:
        if str(x).count("1") == 0:
            if len(f(x)) > 0:
                print(x, log(x-f(x)[0], 3))
                k+=1
