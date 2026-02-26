from itertools import product
k = 0
s = "АБВОСТУ"
for w1 in product(s, repeat=5):
    k += 1
    w = ''.join(w1)
    if w.count("А") == 0 and w.count("О") == 0:
        if len(w) == len(set(w)):
            if w.endswith("СБ"):
                print(k, w)
                break
