def f(n):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + bin((n%3+1)*3)[2:]
    return int(r, 2)
for n in range(1, 600):
    if f(n) <= 416:
        print(f(n))
