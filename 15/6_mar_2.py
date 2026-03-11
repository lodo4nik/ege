for a in range(0, 10000):
    f = 1
    for x in range(15, 31):
        f = f*((x&29==0) or ((x&11==0) <= (x&a!=0)))
        if f == 0:
            break
    if f == 1:
        print(a)
        break
