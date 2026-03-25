with open("sbornik_1.txt") as f:
    s = f.readline()

m = 0
for l in range(len(s)):
    for r in range(l+m, len(s)):
        c = s[l:r+1]
        if c[0] != "S" or c.count("1")+c.count("3")+c.count("5")+c.count("7")+c.count("9")>35:
            break
        else:
            if c.count("1")+c.count("3")+c.count("5")+c.count("7")+c.count("9")==35:
                if c[1:].count("S") == 0:
                    m = max(m, len(c))
    if l%100000==0: print(l, len(s), m)

print(m)
