def f(n):
    r = bin(n)[2:]
    if n % 7 == 0:
        r = r[0:3] + r
    else:
        r = r + bin((n % 7)*7)[2:]

    return int(r, 2)

rs = []

for n in range(1, 999, 2):
    if f(n) < 419:
        rs.append(n)

print(f(45))
