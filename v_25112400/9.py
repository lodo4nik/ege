f = open("9.txt")
k = 0
for line in f:
    n = [int(i) for i in line.split()]
    n1 = [i for i in n if n.count(i) == 1]

    if len(n1) == 5:
        if max(n1)+min(n1) <= sum(n1)-(max(n1)+min(n1)):
            k += 1
print(k)