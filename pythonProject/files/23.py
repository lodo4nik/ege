n = 36**7 + 6**19 - 18

while n != 0:
    ost = n % 6
    n //= 6
    if ost == 0:
        print(1)