# https://education.yandex.ru/ege/inf/task/1452a6ee-c08b-4f20-8169-6fe1a281193d
p = set(range(15, 41))
q = set(range(21, 64))
a = set()

for x in range(-10000, 10000):
   f = ((x in p) <= (((x in q) and (x not in a)) <= (x not in p)))
   if f == 0:
       a.add(x)

print(a)
