with open("test_17.txt") as f:
    nums = [int(i) for i in list(f)]

pars = []

min_dvuzn = min([i for i in nums if len(str(i)) == 2])
for i in range(len(nums)-1):
    if (len(str(nums[i])) == 3 or len(str(nums[i+1])) == 3) and (nums[i] + nums[i+1]) % min_dvuzn == 0:
        pars.append(nums[i] + nums[i+1])

print(len(pars), max(pars))