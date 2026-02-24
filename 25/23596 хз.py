def f(x):
    divs = []
    for div in range(2, int(x**0.5)+1):
        if x % div == 0:
            divs.append(div)
            if div != x//div:
                divs.append(x//div)
    return divs


for x in range(82_871_500, 1, -1):
    divs = f(x)
    if len(divs) >= 4:
        divs = sorted(divs)
        m = divs[0] + divs[1] + divs[-1] + divs[-2]
        if len(f(m)) == 0:
            m = str(m)
            if m[0] + m[-2] == "17":
                print(x, m)