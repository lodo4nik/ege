import math
with open("4_17.txt") as f:
    nums = [int(i) for i in list(f)]

pars = []


max_sq = (max([i for i in nums if abs(i) % 10 == 3]))**2
for i in range(len(nums)-1):
    if ((abs(nums[i]) % 10 == 3) and (abs(nums[i+1]) % 10 != 3) or (abs(nums[i]) % 10 != 3) and (abs(nums[i+1]) % 10 == 3)):
        if nums[i]**2 + nums[i+1]**2 >= max_sq:
            pars.append(nums[i]**2 + nums[i+1]**2)

print(len(pars), max(pars))