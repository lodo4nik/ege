# https://education.yandex.ru/ege/inf/task/1b9fb0ec-40fb-4450-be95-e7bae137b1da
cnt = 0
s = "АКЛМНЯ"
for s1 in s:
    for s2 in s:
        for s3 in s:
            for s4 in s:
                for s5 in s:
                    w = s1 + s2 + s3 + s4 + s5
                    if s1 == "М" and s2 == "Н":
                        cnt += 1
                        print(w)
print(cnt)