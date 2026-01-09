def to_three(x):
    s = ''
    while x:
        s = str(x % 3) + s
        x //= 3
    return s

for n in range(1, 1000):
    n3 = to_three(n)
    if n % 5 == 0:
        n3 = n3 + n3[-2:]
    else:
        n3 = n3 + to_three(n % 5 * 7)

    if int(n3, 3) <= 273:
        print(n)