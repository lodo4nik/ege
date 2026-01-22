from itertools import permutations
table = '567 34 247 235 14 17 136'.split()
graph = 'FA FG GA AD DB GE BE BC CE'.split()
print('1 2 3 4 5 6 7')
for p in permutations('ABCDEFG'):
    if all(str(p.index(c2)+1) in table[p.index(c1)] for c1, c2 in graph):
        print(*p)
        break