# https://education.yandex.ru/ege/inf/task/78b6e053-eaf4-40bc-a7d1-53fad9f7eee4

from itertools import product
s = "АБРТЫ"

for n, s in enumerate(product(s, repeat=5)):
    w = ''.join([i for i in s])
    if w.count("Ы") == 0:
        if w.count("АА") == 0:
            print(n+1, w)
            exit()