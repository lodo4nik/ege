for a in range(-200, 200):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            if not((x>39) or (y > 26) or ((2*x + 4*y) < a)):
                flag = False
                break
            if not flag:
                break
    if flag:
        print(a)