s = "АЕКНС"
cnt = 0
for s1 in s:
    for s2 in s:
        for s3 in s:
            for s4 in s:
                for s5 in s:
                    for s6 in s:
                        cnt+=1
                        word = s1+s2+s3+s4+s5+s6
                        if word == "СЕНЕКА":
                            print(cnt, word)