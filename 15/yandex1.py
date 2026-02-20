# https://education.yandex.ru/ege/inf/task/9f4505bf-95bb-4dd3-907f-06267d06267e

k = 0

for x in range(0, 20):
   if not((x not in [2, 12, 4, 1, 13]) and (x not in [13, 35, 4, 1, 81, 9]) or (x in [35, 2, 10, 15])):
       k += 1

print(k)
