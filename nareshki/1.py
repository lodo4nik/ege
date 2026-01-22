from itertools import permutations

table = '47 56 46 137 267 235 135'.split()
graph = 'АБ АВ БГ БД ВЕ ВК ГД ЕК ДЕ'.split()

print("1 2 3 4 5 6 7")
for p in permutations("АБВГДЕК"):
    if all(str(p.index(c2)+1) in table[p.index(c1)] for c1, c2 in graph):
        print(*p)
        break