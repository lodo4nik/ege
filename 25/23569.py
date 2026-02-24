def f(x):
    divs = []
    for div in range(2, int(x**0.5)+1):
        if x % div == 0:
            divs.append(div)
            divs.append(x//div)
    return divs

for x in range(6_086_055, 6_096_055):
    divs = f(x)
    if len(divs) == 2:
        p_divs = [i for i in divs if len(f(i)) == 0 and str(i).count("6") == 1]
        if len(p_divs) == 2:
            print(x, max(divs))