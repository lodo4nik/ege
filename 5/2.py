# https://education.yandex.ru/ege/inf/task/2330b1ca-d047-4466-a7a1-b0ff32db6318

reses = []
for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        ost = bin(n % 3 * 3)[2:]
        r = r + ost

    res = int(r, 2)
    if res >= 195:
        reses.append(res)

print(min(reses))