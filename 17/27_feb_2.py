with open("27_feb_2.txt") as f:
    nums = [int(i) for i in f]
    reses = []
    for i in range(1, len(nums)):
        a = nums[i-1]
        b = nums[i]
        if abs(a-b) % 2 == 0 and abs(a-b) % 37 == 0:
            reses.append(a+b)

print(len(reses), max(reses))
