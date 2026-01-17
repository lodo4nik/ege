def to_seven(x):
    a = ''
    while x:
        a = str(x % 7) + a
        x //= 7
    return a

for n in range(10000, 1, -1):
    r = to_seven(n)
    if r.count('2') % 2 == 0:
        r += '555'
    else:
        r = '1' + r
    if int(r, 7) < 3799:
        print(n)
        exit()