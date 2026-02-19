for a in range(1, 200):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((x % 30 == 0) and (x % 45 != 0)) <= (x % a != 0)):
                flag = False
                break
            if not flag:
                break
    if flag:
        print(a)


## НЕВЕРНО НЕВЕРНО НЕВЕРНО