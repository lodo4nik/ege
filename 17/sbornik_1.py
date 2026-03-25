with open("17var01.txt") as f:
    nums = [int(i) for i in f]

mini = min([i for i in nums if len(str(abs(i)))==2])
maxi = max([i for i in nums if len(str(abs(i)))==2])

m = mini+maxi
reses=[]
for i in range(2, len(nums)):
    a = nums[i-2]
    b = nums[i-1]
    c = nums[i]
    dvuh = [i for i in [a, b, c] if len(str(abs(i)))==2]
    if len(dvuh) >= 2:
        if a+b+c>m:
            reses.append(a+b+c)

print(len(reses), max(reses))
