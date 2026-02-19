s = "24*68?35"


for x in range(2468035//13*13, 10**9, 13):
    s = str(x)
    if s[0:2] + s[-5:-3] + s[-2:] == "246835":
        if int(s[-3]) % 3 == 0:
            if int(s[-3]) % 2 != 0:
                if s[2:-5] == "" or len([i for i in s[2:-5] if int(i) % 2 == 0]) == len(s[2:-5]):
                    print(x, x//13)