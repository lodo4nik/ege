with open("9_3_mar_statgrad.txt") as f:
    k = 0
    suma = 0
    for line in f:
        k+=1
        if k % 2 == 0:
            n = [int(i) for i in line.split()]
            sr = sum(n) // len(n)
            n1 = [i for i in n if i == sr]
            if len(n1) > 0:
                kv = [i for i in n if i**0.5 == int(i**0.5)]
                if len(kv) > 0:
                    suma+=k
    print(suma)
