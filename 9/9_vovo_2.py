f = open("9_vovo_2")
sums = []

for line in f:
    a = sorted([int(i) for i in line.split()])
    inpars = 0
    # print(a, set(a))
    for i in set(a):
        if a.count(i)//2:
            inpars += a.count(i)//2
    if inpars >= 3:
        # print(a, inpars)
        sums.append(sum(a))
        print(a, inpars)

print(min(sums))