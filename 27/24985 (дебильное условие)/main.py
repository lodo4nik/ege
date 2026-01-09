from math import dist
file = open("27B_24985.txt")

data = []
for line in file:
    x, y = [float(i) for i in line.split()]
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
print([len(cl) for cl in clusters])

def ancentr(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return max(m)[1]

c0 = ancentr(clusters[0])
c1 = ancentr(clusters[1])
c2 = ancentr(clusters[2])

q1 = int(abs(dist(c1, c2) * 10000))

# максимальное расстояние от антицентра кластера до точки этого же кластера среди всех кластеров
q2 = int(max([max(dist(ancentr(cl), p) for p in cl) for cl in clusters])*10000)
print(q1, q2)