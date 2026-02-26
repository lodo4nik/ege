for a in range(-100, 100):
    f = 1
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = f*((x<9) <= ((5*y<x) <= (2*x*y < a)))
            if f == 0:
                break
    if f == 1:
        print(a)
        break
