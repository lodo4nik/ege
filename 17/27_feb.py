with open("27_feb.txt") as f:
    nums = [int(i) for i in f]
    reses = []
    maxi = max([i for i in nums if len(str(i)) == 3])
    for i in range(1, len(nums)):
        a = nums[i-1]
        b = nums[i]
        treh = [i for i in [a, b] if len(str(i)) == 3]
        if len(treh) == 1:
            if a+b >= maxi:
                reses.append(a+b)

print(len(reses), max(reses))
