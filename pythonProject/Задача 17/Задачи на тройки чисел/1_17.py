with open("1_17.txt") as f:
    nums = [int(i) for i in list(f)]

pars = []

min_dvuzn = (max([i for i in nums if ((abs(i) % 100 == 15) and (len(str(abs(i))) == 3))]))**2
for i in range(len(nums)-2):
    test = []
    if (nums[i] >= 0 and nums[i+1] >= 0 and nums[i+2] >= 0) or (nums[i] < 0 and nums[i+1] < 0 and nums[i+2] < 0):
        test.append(nums[i])
        test.append(nums[i+1])
        test.append(nums[i+2])
        print(test)
        if min(test) * max(test) > min_dvuzn:
            pars.append(min(test) * max(test))

print(len(pars), min(pars))