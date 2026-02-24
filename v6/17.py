with open("17.txt") as f:
    answs = []
    
    nums = [int(i) for i in f]
    for i in range(1, len(nums)):
        a = nums[i-1]
        b = nums[i]
        if str(a**2 + b ** 2).endswith("3"):
            answs.append([a, b])

print(answs)
for i in answs:
    i.append(i[0] + i[1])

minsum = 99999999
for i in answs:
    if i[2] < minsum:
        minsum = i[2]
#    if minsum == -186259:
#        print(i)


# [-91402, -94857, -186259]i

# хрен его знает короче

print(len(answs), abs(max([-91402, -94857])))
