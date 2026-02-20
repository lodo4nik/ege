# https://education.yandex.ru/ege/inf/task/691e4108-0628-4175-90d1-827c5a8b5a94
b = set(range(70, 81))
k = 0
for a in range(1, 1000):
   f = 1
   for x in range(1, 1000):
       if f*((x % 12 == 0) and (x in b) and (x % a != 0)) == 1:
           f = 0
           break
   if f == 1: k+=1

print(k)
