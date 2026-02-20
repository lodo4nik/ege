# https://education.yandex.ru/ege/inf/task/9ccc8672-6a8a-463b-ba41-2b379480b4b9
b = {-42, -10, -8, 2, 16}
c = {-10, -4, 2, 15, 23}
a = {}

for x in range(-10000, 10000):
    f = ((x in a) <= (x in b)) or (x in c)
    if f == 0:
        a.add(x)

print(a)
### НЕВЕРНО НЕВЕРНО НЕВЕРНО