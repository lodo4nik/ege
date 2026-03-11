from string import printable
from itertools import product
s = printable[:12]
print(s)
k = 0
for s1 in s[1:]:
    for s2 in s:
        for s3 in s:
            for s4 in s:
                for s5 in s:
                    w = s1+s2+s3+s4+s5
                    ch = [i for i in w if i in "02468a"]
                    odinak = [i for i in ch if ch.count(i) == 3]
                    if len(ch) == 3 and len(odinak) == 3:
                        if w.count("000") == 1 or w.count("222") == 1 \
                           or w.count("444") == 1 or w.count("666") == 1 \
                           or w.count("888") == 1 or w.count("aaa") == 1:
                            k+=1

print(k)
