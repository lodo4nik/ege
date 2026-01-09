from functools import lru_cache

@lru_cache(None)
def f(a, b):
    if a+b >= 75:
        return 0
    t = [f(a+1, b), f(a*2, b), f(a, b+1), f(a, b*2)]
    n = [i for i in t if i <= 0]

    if n:
        return -max(n) + 1
    else:
        return -max(t)

ans_19 = []

for i in range(1, 67):
    if f(8, i) == 2:
        print("20", i)
    if f(8, i) == -2:
        print("21:", i)
    if f(8, i+1)==1 or f(8, i*2)==1 or f(9, i)==1 or f(16, i)==1:
        ans_19.append(i)

print("19", ans_19)