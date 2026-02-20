# https://education.yandex.ru/ege/inf/task/bbdc7a8c-b582-469b-95a3-c0c2de99b8d4
##A = []
##for a in range(1, 10000):
##    A.append(a)
##    flag = 1
##    for x in range(1, 10000):
##        flag = flag*(x in [14, 16, 18, 20, 22, 24]) <= (((x in [16, 19, 22, 25, 28]) and (x not in A)) <= (x not in [14, 16, 18, 20, 22, 24]))
##        if not flag:
##             break
##    if flag:
##        print(sum(A))
##        break
# НЕВЕРНО НЕВЕРНО НЕВЕРНО
