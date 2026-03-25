with open("24_14510.txt") as f:
    s = f.readline()

print("done")
m = 10000
for l in range(len(s)):
    for r in range(l+m, l, -1):
        c = s[l:r+1]
        k = 0
        for i in range(2, len(c)):
            a = c[i-2]
            b = c[i-1]
            g = c[i]
            if a not in "aeiouy" and b not in "aeiouy" and g in "aeiouy":
                k+=1
        if k >= 500:
            m = min(m, len(c))
        if k < 500:
            break
    if l%100000==0: print(l, len(s), m)

print(m)
