from string import printable

def to_twelve(x):
    s = ''
    while x:
        s = printable[x%12] + s
        x //= 12
    return s


def f(n):
    r = to_twelve(n)
    if n % 3 == 0:
        r = "b" + r + "2"
    else:
        r = "1" + r + "0"
    return int(r, 12)

rs = []
for n in range(1, 1000):
    if f(n) > 2500:
        rs.append(f(n))

print(min(rs))
