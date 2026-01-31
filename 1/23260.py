from itertools import permutations

table = '346 348 12 127 678 15 458 257'.split()
graph = 'DC DB DA BC BH CF FG HG AH AE EG'.split()

print("1 2 3 4 5 6 7 8")

for p in permutations("ABCDEFGH"):
    if all(str(p.index(c2) + 1) in table[p.index(c1)] for c1, c2 in graph):
        print(*p)