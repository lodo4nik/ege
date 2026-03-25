def fd(x):
    divs = []
    for div in range(2, int(x**0.5)+1):
        if x % div == 0:
            divs.append(div)
            divs.append(x//div)
    return(list(set(divs)))

a = set(range(3, 61))
b = fd(177)

for y in range(1, 5000):
    c = fd(y)
    f = 0
    if len(c)>0:
        f = 1
        for x in range(-10000, 10000):
            f = f*((x in c) <= ((x in a) and (x not in b)))
            if f == 0: break
    if f == 1:
        print(y)
