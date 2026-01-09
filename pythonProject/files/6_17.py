with open("6_17.txt") as f:
    nums = [int(i) for i in list(f)]

pars = []

min_dvuzn = min([i for i in nums if len(str(abs(i))) == 2])
for i in range(len(nums)-1):
    if len(str(abs(nums[i]))) == 3 or len(str(abs(nums[i+1]))) == 3:
        if nums[i] + nums[i+1] < min_dvuzn:
            pars.append(nums[i] + nums[i+1])

print(len(pars), max(pars))