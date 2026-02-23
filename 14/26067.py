from string import printable

def to_nine(x):
    s = ''
    while x:
        s = printable[x%9] + s
        x //= 9
    return s

for x in range(50_000, 1, -1):
    a = 5 * 9**5 + 3 * 9**4 + 7 * 9**3 + 4 - x
    a9 = to_nine(a)
    if a9.count("1") == 4:
        print(x)
        break
