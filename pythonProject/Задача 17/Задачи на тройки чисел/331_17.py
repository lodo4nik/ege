with open("331_17.txt") as f:
    nums = [int(i) for i in list(f)]

pars = []

min_dvuzn = max([i for i in nums if abs(i) % 100 == 21])
for i in range(len(nums)-2):
    if ((len(str(abs(nums[i]))) == 3) + (len(str(abs(nums[i+1]))) == 3) + (len(str(abs(nums[i+2]))) == 3)) == 2:
        if nums[i] + nums[i+1] + nums[i+2] <= min_dvuzn:
            pars.append(nums[i] + nums[i+1] + nums[i+2])

print(len(pars), max(pars))