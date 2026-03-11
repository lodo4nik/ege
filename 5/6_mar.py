def f(n):
    r = bin(n)[2:]
    if n % 2 != 0:
        r = "10" + r[:-2] + "01"
    else:
        r = "11" + r[2:] + "1"
    return int(r, 2)

rs = []
for n in range(42, 10000):
    rs.append(f(n))
print(min(rs))
