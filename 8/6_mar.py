from itertools import product
s = "АЁРТШ"
k = 0
for w1 in product(s, repeat=5):
    k += 1
    w = ''.join(w1)
    if w.count("А") <= 1 and w.count("ЁЁ") == 0:
        print(k, w)
        break
