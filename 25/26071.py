def f(x):
    divs = []
    for div in range(2, int(x**0.5)+1):
        if x % div == 0:
            divs.append(div)
            divs.append(x//div)
    return divs

for i in range(2_000_000, 2_010_000):
    divs = f(i)
    endswith37 = [n for n in divs if n != 37 and str(n).endswith("37") and len(f((i // n))) == 0]
    endswith372 = [n for n in divs if n != 37 and str(n).endswith("37")]
    if len(endswith37) >= 1:
        print(i, min(endswith372))
