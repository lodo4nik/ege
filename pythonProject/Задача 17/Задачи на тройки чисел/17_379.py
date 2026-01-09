with open("17-379.txt") as f:
    nums = [int(i) for i in list(f)]

pars = []

min_dvuzn = max([i for i in nums if i % 100 == 15])
for i in range(len(nums)-2):
    if ((len(str(abs(nums[i]))) == 4) + (len(str(abs(nums[i+1]))) == 4) + (len(str(abs(nums[i+2]))) == 4)) == 1:
        if nums[i] + nums[i+1] + nums[i+2] >= min_dvuzn:
            pars.append(nums[i] + nums[i+1] + nums[i+2])

print(len(pars), max(pars))