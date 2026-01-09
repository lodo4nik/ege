from functools import lru_cache

@lru_cache(None)
def f(a, b):
    if a+b >= 49:
        return 0
    t = [f(a+1, b), f(a*3, b), f(a, b+1), f(a, b*3)]
    n = [i for i in t if i <= 0]

    if n:
        return -max(n) + 1
    else:
        return -max(t)

ans_19 = []

for i in range(1, 43):
    if f(5, i) == 2:
        print("20", i)
    if f(5, i) == -2:
        print("21:", i)
    if f(5, i+1)==1 or f(5, i*2)==1 or f(6, i)==1 or f(15, i)==1:
        ans_19.append(i)

print("19", min(ans_19))