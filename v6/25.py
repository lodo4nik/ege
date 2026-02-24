def f(n):
    divs = []
    for div in range(2, int((n**0.5))+1):
        if n % div == 0:
            divs.append(div)
            divs.append(n//div)
    return divs

for x in range(2_460_070, 2_470_000):
    divs = f(x)
    ends17 = [i for i in divs if i != x and i != 13 and str(i).endswith("13")]
    if len(ends17) > 0:
        print(x, min(ends17))
