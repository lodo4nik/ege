for a in range(1, 1000000):
    f = 1
    for x in range(1, 1000000):
        f = f*((((x%36==0) and (x%42==0)) <= (x%a==0)) and (a*(a-25) < 25*(a+200)))
        if f == 0:
            break
    if f == 1:
        print(a)
