def dist(p, p1):
    x1, y1 = p
    x2, y2 = p1
    return abs(x2-x1) + abs(y2-y1)

file = open("27B_24670.txt")

data = []
for line in file:
    x, y = [float(i) for i in line.split()]
    data.append([x, y])
print(len(data))

clusters = []
while data:
    cl = [data.pop(0)]
    for p in cl:
        neighbors = [p1 for p1 in data if dist(p, p1) < 2]
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

c0 = centr(clusters[0])
c1 = centr(clusters[1])
c2 = centr(clusters[2])

px = int((c0[0]+c1[0]+c2[0])/3*10000)
py = int((c0[1]+c1[1]+c2[1])/3*10000)

print(px, py)