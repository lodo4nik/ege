with open("sbornik_1.txt") as f:
    k = 0
    for line in f:
        k+=1
        s = [int(i) for i in line.split()]
        a3 = [i for i in s if s.count(i) == 3]
        a1 = [i for i in s if s.count(i) == 1]
        if len(a3) == 3 and len(a1) == 4:
            if sum(a1) > sum(a3):
                print(k)
