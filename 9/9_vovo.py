from itertools import permutations

maxi = 0
i = 0

f = open("9_vovo")
for line in f:
    i += 1
    a = [int(i) for i in line.split()]
    a_even = [i for i in a if i % 2 == 0]
    a_odd = [i for i in a if i % 2 != 0]
    if len(a_even) == len(a_odd):
        suma = sum(a)
        if suma % 3 == 0:
            tg = suma // 3

            found = False
            for p in permutations(a):
                if p[0] + p[1] == tg and p[2] + p[3] == tg and p[4] + p[5] == tg:
                    found = True
                    break
            if found == True:
                maxi = i

print(maxi)