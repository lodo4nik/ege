with open("24_27634.txt") as f:
    s = f.readline()
    
m = 99999999999999

for l in range(len(s)):
    for r in range(l, len(s)):
        c = s[l:r+1]
        if c.count("Z") >= 270:
            m = min(m, len(c))
print(m)
