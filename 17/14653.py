with open("14653.txt") as f:
    s = [int(i) for i in f]
    n = []
    k69 = max([i for i in s if str(i).endswith("69")])
    s_plus_k17 = sorted([i for i in s if i > 0 and i % 17 == 0])
    minis = s_plus_k17[0] + s_plus_k17[1]
    for i in range(3, len(s)):
        a = s[i-3]
        b = s[i-2]
        c = s[i-1]
        d = s[i]
        ch = [a, b, c, d]
        tresh = [i for i in ch if len(str(abs(i))) == 3]
        k18 = [i for i in ch if i % 18 == 0]
        if len(tresh) == 2 and len(k18) == 1:
            if sum(ch) % minis == 0:
                if a * b * c * d <= k69**2:
                    n.append((sum(ch))**2)
print(len(n), min(n))
