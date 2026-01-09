# https://education.yandex.ru/ege/inf/task/783a4cad-5d6e-49b9-a85d-82e9895d80ad
cnt = 0
first = 0
end = 0
s = "ЕКОФ"
for s1 in s:
    for s2 in s:
        for s3 in s:
            for s4 in s:
                for s5 in s:
                    w = s1+s2+s3+s4+s5
                    cnt += 1
                    if w.count("О") == 1:
                        if w.count("ОК") == 0 and w.count("КО") == 0 and w.count("ОФ") == 0 and w.count("ФО") == 0:
                            if first == 0:
                                first = cnt
                            end = cnt

print(first, end)