# https://education.yandex.ru/ege/inf/task/a3f9018d-89cc-4d24-aedc-c9f5f8ed19b3

for a in range(4, 93):
    always_false = 1
    for x in range(1, 10000):
        f = ((x & 46 != 0) <= ((x & a != 0) <= (x & 70 != 0))) <= ((x & 6 == 0) and (x & a != 0) and (x & 70 == 0))
        if f == 1:
            always_false = 0
            break
    if always_false == 1:
        print(a)
