def f(n, p=2):
    for i in range(p, int(n**0.5) + 1):
        if n % i == 0: 
            return [i] + f(n // i, i)
    return [n]

for i in range(5_000_001, 5_100_000):
    mnoj = f(i)
    if len(mnoj) == 3:
        has_twothree = [i for i in mnoj if ("2" in str(i)) or ("3" in str(i))]
        if len(has_twothree) == 3:
            print(i)
