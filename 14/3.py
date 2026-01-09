# https://education.yandex.ru/ege/inf/task/39991489-2021-4ee7-96a1-f45152dbfcd2



for x in range(0, 10000):
    count2 = 0
    count8 = 0
    a = 9**1942 + 9 * 6**971 + 214 - x

    while a > 0:
        ost = a % 9
        if ost == 2:
            count2 += 1
        if ost == 8:
            count8 += 1
        a //= 9    

    if abs(count2-count8) == 471:
        print(x)
        exit()