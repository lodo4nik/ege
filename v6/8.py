from itertools import product

k = 0
s = "АВСТРИЯ"
for s1 in product(s, repeat=7):
    w = ''.join(s1)
    if w.count("В") <= 3:
        gl = [i for i in w if i in "АИЯ"]
        if len(gl) > 0 and len(gl) % 2 == 0:
            k += 1
print(k)
