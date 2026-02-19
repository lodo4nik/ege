def gen_r(n):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = "10" + r
    else:
        r = "1" + r + "01"
    return int(r, 2)

for n in range(1, 10000000000):
    if gen_r(n) < 30:
        print(n)