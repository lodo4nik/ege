from itertools import product

s = sorted("СТРЕЛА")
k = 0
for w1 in product(s, repeat=5):
    k+=1
    w = ''.join(w1)
    if k%2 == 0:
        if w[0] not in "АСТ":
            if w.count("ЛЛ") == 0:
                if w.count("Л") == 2:
                    print(k, w)
