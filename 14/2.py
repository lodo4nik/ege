for x in range(0, 2031):
    a = 3**100 - x
    cnt = 0
    while a != 0:
        d = a % 3        
        a //= 3
        if d == 0:
            cnt += 1
    if cnt == 5:
        print(x)