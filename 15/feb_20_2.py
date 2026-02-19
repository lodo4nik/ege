for a in range(1, 200):
    flag = True
    for x in range(1, 10000):
        if not(((x % 30 == 0) and (x % 45 != 0)) <= (x % a != 0)):
            flag = False
            break
    if flag:
        print(a)
        break


## ВЕРНО ВЕРНО ВЕРНО