answs = []
for n in range(2, 10000):
    r = bin(n)[2:]
    for code in range(2):
        if r[-1] == r[-2]:
            r = r + "0"
        else:
            r = r + "1"
    
    ans = int(r, 2)
    if ans > 93:
        answs.append(n)

print(min(answs))