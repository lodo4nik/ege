def f(x):
    divs = []
    for div in range(2, int(x**0.5)+1):
        if x % div == 0:
            divs.append(div)
            divs.append(x//div)
    return divs

k = 0
for x in range(1_324_728, 1_400_000):
    if k <= 5:
        divs = f(x)
        if len(divs) == 2:
            has_five = [i for i in divs if str(i).count("5") == 1]
            if len(has_five) == 2:
                print(x, divs)
                k+=1