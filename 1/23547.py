from itertools import permutations, repeat

table = "24 134 267 125 47 37 356".split()
graph = "AF AG FG GE FC EB BC CD DC".split()

print("1 2 3 4 5 6 7")

for p in permutations("ABCDEFG"):
    if all(str(p.index(c2) + 1) in table[p.index(c1)] for c1, c2 in graph):
        print(p)