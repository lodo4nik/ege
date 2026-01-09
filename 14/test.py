for n in range(8, 10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + "00"
    else:
        r = r + "10"

    if r.count("1") % 2 == 0:
        r = r[:-3] + "101"
    else:
        r = r[:-3] + "010"

    if int(r, 2) > 210:
        print(n)
        exit()