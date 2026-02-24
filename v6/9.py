with open("9.txt") as f:
    k = 0
    for line in f:
        s = [int(i) for i in line.split()]
        s1 = s[:]
        maxi = max(s)
        mini = min(s)
        s1.remove(maxi)
        s1.remove(mini)
        if (maxi**2 + mini**2) <= (sum(s1))**2:
            k+=1
    print(k)
