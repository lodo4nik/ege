with open("17.txt") as f:
    nums = [int(i) for i in list(f)]

pars = []

for i in range(len(nums)-1):
    if (nums[i] - nums[i+1]) % 2 == 0:
        if nums[i] % 31 == 0 or nums[i+1] % 31 == 0:
            pars.append(nums[i] + nums[i+1])

print(len(pars), max(pars))