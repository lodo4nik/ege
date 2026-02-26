# 
#
k = 0
for x in range(2*(10**8)//42*42, 1 , -42):
    if k < 5:
        if x <= 2*(10**8):
            s = str(x)
            if s[1] + s[-1] == "20" and ("4" in s[2:-1]):
                if (not (s[0] == "1" and ("7" in s[1:]))):
                    print(x, x//42)
                    k += 1

