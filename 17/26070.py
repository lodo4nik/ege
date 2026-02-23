with open("17.txt") as f:
    answs = []
    
    nums = [int(i) for i in f]
    maxi = max([i for i in nums if i % 37 == 0 and str(i).endswith("6")])
    for i in range(2, len(nums)):
        a = nums[i-2]
        b = nums[i-1]
        c = nums[i]
        trehs = [i for i in [a, b, c] if len(str(abs(i))) == 3]
        if len(trehs) == 0:
            if a + b + c < maxi:
                answs.append(a+b+c)

print(len(answs), max(answs))
