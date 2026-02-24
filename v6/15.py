for a in range(1, 10000):
    f = 1
    for x in range(1, 10000):
        f = f*(((20+a+3*x)>(800-a)) and ((a % 100) + (120 % a) > 180))
        if f == 0:
            break
    if f == 1:
        print(a)
        break
