f = open("25348.txt")
lines = []
for line in f:
    lines.append(line.split())

k = 0
for line in lines:
    s = [int(i) for i in line]
    s3 = [i for i in s if s.count(i) == 3]
    s1 = [i for i in s if s.count(i) == 1]
    if len(s3) == 3 and len(s1) == 4:
        if max(s) in s1:
            k += 1

print(k)