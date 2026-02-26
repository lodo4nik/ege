from string import printable
maxes = []
# [20, 13, 7]
for x in printable[0:14]:
    for y in printable[0:14]:
        s1 = int(f"14{y}5{x}2", 14)
        s2 = int(f"31{x}2{y}3", 14)
        s = s1 + s2
        if int(x, 14) == 13 and int(y, 14) == 7:
            print(s/9)
        if s % 9 == 0:
            maxes.append([int(x, 14) + int(y, 14), int(x, 14), int(y, 14)])
print(sorted(maxes))
