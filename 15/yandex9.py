# https://education.yandex.ru/ege/inf/task/8f13d075-e784-4654-ae10-7d109cee90e9

for a in range(0, 1000):
    always_false = 1
    for x in range(0, 1000):
        for y in range(0, 1000):
            f = ((3*x + y) > a) and (y < x) and (x < 30)
            if f == 1:
                always_false = 0
                break
        if always_false == 0:
            break
    if always_false == 1:
        print(a)
        break
