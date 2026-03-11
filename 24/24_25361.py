with open("24_25361.txt") as f:
    s = f.readline()

for c in "02468":
    s = s.replace(c, "0")
m = 0
for l in range(len(s)):
    for r in range(l+m, len(s)):
        c = s[l:r+1]
        if c.count("0") == 1:
            if c[0] == "0":
                if c.count("F") == 76:
                    m = max(m, len(c))
        else:
            break
print(m)
