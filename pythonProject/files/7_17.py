with open("7_17.txt") as f:
    nums = [int(i) for i in list(f)]

pars = []

min_sto = len([i for i in nums if i % 100 == 0])
for i in range(len(nums)-1):
    if nums[i] < 0 or nums[i+1] < 0:
        if nums[i] + nums[i+1] < min_sto:
            pars.append(nums[i] + nums[i+1])

print(len(pars), abs(max(pars)))