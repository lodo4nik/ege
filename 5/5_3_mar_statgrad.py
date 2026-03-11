from math import *
def f(n):
    nums = [int(i) for i in str(n)]
    p = prod([i for i in nums if i != 0])
    m = min(nums) + max(nums)

    t1 = p+m
    t2 = p*m
    r = list(sorted([t1, t2]))
    r1 = ''.join([str(i) for i in r])

    return r1

for n in range(1, 10001):
    if f(n) == "23126":
        print(n)
