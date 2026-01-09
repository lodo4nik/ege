k = []
for s in open("C:/Users/dog/Documents/GitHub/ege/9/24359.txt"):
    a = [int(i) for i in s.split()]
    a3 = [i for i in a if a.count(i) == 3]
    a2 = [i for i in a if a.count(i) == 2]
    a1 = [i for i in a if a.count(i) == 1]
    if len(a3) == 3 and len(a2) == 2 and len(a1) == 3:
        if sum(a3 + a2) > sum(a1):
            k.append(sum(a))
print(k)