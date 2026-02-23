for a in range(34500, 34570):
    f = 1
    for x in range(1, 10000):
        for y in range(1, 10000):
            f=f*((34567 != (y + 3*x)) or ((a > x) and (a > y)))
            if f == 0:
                break
    if f == 1:
        print(a)
# это нужно руками считать я не помню как
