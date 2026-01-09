f = open("17_24074.txt")

s = [int(i) for i in f]

mz = min([i for i in s if len(str(i)) == 3 and str(i).endswith("9")])

answs = []
for i in range(1, len(s)-1):
    if len(str(s[i])) == 2 or len(str(s[i+1])) == 2:
        if (s[i] + s[i+1]) % mz == 0:
            answs.append(s[i] + s[i+1])

print(len(answs), max(answs))