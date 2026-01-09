with open("5_17.txt") as f:
    nums = [int(i) for i in list(f)]

pars = []

min_dvuzn = (min([i for i in nums if abs(i) % 10 == 3]))**3
for i in range(len(nums)-1):
    if ((abs(nums[i]) % 10 == 6) and (abs(nums[i+1]) % 10 == 6)):
        if nums[i]**2 + nums[i+1]**2 >= min_dvuzn:
            pars.append(nums[i]**2 + nums[i+1]**2)

print(len(pars), max(pars))