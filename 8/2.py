s = "ДРС"
cnt = 0
for s1 in s:
    for s2 in s:
        for s3 in s:
            word = s1+s2+s3
            if word[0] == "С":
                cnt += 1
                
print(cnt)