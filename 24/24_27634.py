with open("24_27634.txt") as f:
    s = f.readline()
    
m = 10000
for l in range(len(s)):
    for r in range(l+m, l, -1):
        c = s[l:r+1]
        if c.count("Z") >= 270:
            m = min(m, len(c))
        else:
            break
    if l%100000==0: print(l, len(s), m)
print(m)
