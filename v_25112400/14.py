s = 5*729**2024 + 3*243**1413 - 7*81**169 - 2*9**107 + 3017

osts = []
while s:
    ost = s % 27
    if ost <= 25:
        osts.append(ost)
    s //= 27

print(sum(osts))