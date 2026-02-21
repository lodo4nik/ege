# https://education.yandex.ru/ege/inf/task/020dbd7f-2c15-4a0c-af2c-fea4ab2b122a

for a in range(1, 400):
    f = 1
    for x in range(1, 100000):
        f = f*((not((x % 3 == 0) and (x % 5 == 0))) or (a >= 42 - x))
        if f == 0:
            break
        else: print(a)
