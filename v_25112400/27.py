from math import *

f = open("27B_24117.txt")

data = []
for line in f:
    x, y = (float(i) for i in line.split())
    data.append([x, y])
print(len(data))

clusters = []
while data:
    cl = [data.pop(0)]
    for p in cl:
        neighbors = [p1 for p1 in data if dist(p, p1) < 1]
        for p1 in neighbors:
            cl.append(p1)
            data.remove(p1)
    clusters.append(cl)

def acentr(cl):
    m = []
    for p in cl:
        sm = sum([dist(p, p1) for p1 in cl])
        m.append([sm, p])
    return max(m)[1]

print([len(cl) for cl in clusters])

c1 = acentr(clusters[1])
c2 = acentr(clusters[2])

def max_d(cl):
    md = float(-inf)
    ac = acentr(cl)
    for p in cl:
        d = dist(p, ac)
        if d > md:
            md = d
    return md



q1 = int(dist(c1, c2)*10000)
q2 = int(max(max_d(cl) for cl in (clusters[0], clusters[1], clusters[2]))*10000)


print(q1, q2)