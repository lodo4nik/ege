s = sorted("БУРАТИНО")
k = 0
for x1 in s:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                for x5 in s:
                    w = x1+x2+x3+x4+x5
                    k += 1
                    if k % 2 != 0:
                        if w[0] not in 'УАИО' and len(w) == len(set(w)):
                            print(k, w)