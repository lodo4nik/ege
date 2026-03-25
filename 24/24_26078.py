with open("24_26078.txt") as f:
    s = f.readline()

m = 1000
for l in range(len(s)):
    for r in range(l+m, l, -1):
        c = s[l:r+1]
        if c.count("W") == 90:
            if c.count("2025") >= 110:
                m = min(m, len(c))
        else:
            break
    if l%100000==0: print(l, len(s), m)
print(m)
