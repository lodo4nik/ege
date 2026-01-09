k = 0
for s in open('C:/Users/dog/Documents/GitHub/ege/9/24889.txt'):
    a = [int(i) for i in s.split()]
    a0 = [i for i in a if a.count(i) == 1]
    dummy = a0[:]

    if a.count(max(a)) == 3 and len(a0) == 5 or a.count(max(a)) == 4 and len(a0) == 4:
        dummy.remove(max(a0))
        dummy.remove(min(a0))
        if max(a0)+min(a0) <= sum(dummy):
            print(a, a0, sep=" -> ")
            k +=1
print(k)