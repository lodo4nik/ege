for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + "00"
    else:
        r = r + "11"

    if int(r, 2) > 115:
        print(n)
        exit()