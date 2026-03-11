for a in range(10000, 1, -1):
    f = 1
    for x in range(1, 10000):
        f = f*((x&a!=0) <= ((x&28==0) <= ((x&53!=0) and (x&20==0))))
        if f == 0:
            break
    if f == 1:
        print(a)
        break
