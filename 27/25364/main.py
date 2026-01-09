from math import dist
file = open("27_A_25364.txt")

data = []
for line in file:
    x, y = [float(i) for i in line.replace(",", '.').split()]
    data.append([x, y])
print(len(data))

clusters = []
while data:
    clusters.append([data.pop(0)])
    for p in clusters[-1]:
        neighbors = [p1 for p1 in data if dist(p, p1) < 1]
        clusters[-1].extend(neighbors)
        for p1 in neighbors: data.remove(p1)
    print(len(clusters[-1]))

def centroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


# A
'''
c0 = centroid(clusters[0])
c1 = centroid(clusters[1])

p1 = int(dist((1,1), c0)*10000)
p2 = int(dist((1,1), c1)*10000)

print(p1, p2)
'''

# B
'''
max_cl = clusters[0]
c = centroid(max_cl)

q1 = len([p for p in max_cl if dist(p, c) <= 1.2])
q2 = len([p for p in max_cl if dist(p, c) <= 0.75])

print(q1, q2)
'''