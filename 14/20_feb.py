def to_nine(x):
    s = ''
    while x:
        s = str(x%9) + s
        x //= 9
    return s

reses = []
for x in range(1, 1951):
    a = 72070 + 7400 - x
    reses.append(to_nine(a))

zeros = [i.count("0") for i in reses]
print(max(zeros))