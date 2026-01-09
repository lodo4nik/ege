from math import dist
file = open("27B_18678.txt")

data = []
for line in file:
    x, y = [float(i) for i in line.replace(",", ".").split()]
    data.append([x, y])
print(len(data))

clusters = []
while data:
    cl = [data.pop()]
    for p in cl:
        neighbors = [p1 for p1 in data if dist(p, p1) < 1]
        for p1 in neighbors:
            cl.append(p1)
            data.remove(p1)
    clusters.append(cl)

print([len(cl) for cl in clusters])

def centr(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]

c1 = centr(clusters[0])
c2 = centr(clusters[1])
c3 = centr(clusters[2])

px = int((c1[0]+c2[0]+c3[0])/3*100000)
py = int((c1[1]+c2[1]+c3[1])/3*100000)
print(px, py)