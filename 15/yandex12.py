# https://education.yandex.ru/ege/inf/task/6a427e57-e7bf-417e-a0b0-caac3d5585ec

for a in range(0, 1000):
    f = 1
    for x in range(0, 1000):
        f = f*((x & 52 == 4) <= ((x & 26 == 2) <= (x & a == 6)))
        if f == 0:
            break
    if f == 1:
        print(a)
