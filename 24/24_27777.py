from string import printable

with open("24_27777.txt") as f:
    s = f.readline()
    
##k = 0
##for c in printable:     узнаю че мне там какой срез сделать надо
##    k+=1
##    print(k, c)

for c in printable[38:]:
    s = s.replace(c, "*")

m = 0
for l in range(len(s)):
    for r in range(l+m, len(s)):
        c = s[l:r+1]
        if c.count("*") == 0:
            m = max(m, len(c))
        else:
            break
print(m)
