# https://education.yandex.ru/ege/inf/task/fcd4ef3a-8c80-468a-8217-17f9e35df44d
b = {2, 5, 10, 15, 17, 20, 22, 25}
c = {2, 4, 6, 8, 10, 12, 15, 16, 20, 25}
a = set()

for x in range(-10000, 10000):
   f = ((x in b) == (x in a) and (x in c)) <= ((x in c) == (x in a) and (x in b))
   if f == 0:
       a.add(x)

print(sum(a))
