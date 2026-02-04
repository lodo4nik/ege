def find_divs(x):
    divs = []
    for div in range(2, int(x**0.5)+1):
        if x % div == 0:
            divs.append(div)
            if x//div != div:
                divs.append(x//div)
    return divs


s = '34?8*9'
k = 0

print(s[0:2] + s[3] + s[-1] == "3489")
for x in range(312145, 10**7+1):
    s = str(x)
    if s[0:2] + s[3] + s[-1] == "3489":
        prime_divs = [i for i in find_divs(int(s)) if len(find_divs(i)) == 0]
        if len(prime_divs) > 4:
            k+=1
            print(k, s, max(prime_divs))