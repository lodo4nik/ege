from itertools import product

s = "ВГОРСТ"
n = 0
k = 0
for s in (product(s, repeat=6)):
    n += 1
    w = ''.join(s)
    if n % 2 == 0:
        if w[0:3] == "РОВ":
            if w.count("О") == 3:
                k+=1
                print(n, w)