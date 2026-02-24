s = 5*(729**2024) + 3*(243**1413) - 7*(81**169) - 2*(9**107) + 3017

sss = []
k = 0
while s:
    ost = s % 27
    if ost % 2 == 0:
        sss.append(ost)
    s //= 27

print(sum(sss))
