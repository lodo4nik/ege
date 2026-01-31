from itertools import permutations

table = "345 467 14 123567 147 24 245".split()
graph = "AF AG FG FE GE ED DC CB GB GC GD".split()

print("1 2 3 4 5 6 7")

for p in permutations("ABCDEFG"):
    if all(str(p.index(c2) + 1) in table[p.index(c1)] for c1, c2 in graph):
        print(p)