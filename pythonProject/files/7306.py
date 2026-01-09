s = "УЧЕНИК"
cnt = 0
for s1 in s:
    for s2 in s:
        for s3 in s:
            for s4 in s:
                for s5 in s:
                    w = s1+s2+s3+s4+s5
                    if w[0] == "У" and w[-1] == "К":
                        cnt += 1
print(cnt)