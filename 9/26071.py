with open("9.txt",) as f:
    k = 0
    for line in f:
        a = [int(i) for i in line.split()]
        ch = [i for i in a if i % 2 == 0]
        nch = [i for i in a if i % 2 != 0]
        if sum(ch)>sum(nch):
            if len(nch) > len(ch):
                if (max(ch) + min(nch)) % 3 == 0:
                    k+=1
    print(k)
