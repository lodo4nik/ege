with open("17_3_mar_statgrad.txt") as f:
    nums = [int(i) for i in f]

positives = [i for i in nums if i > 0]
mini = min([i for i in positives if str(i).endswith("99")])

reses = []

for i in range(2, len(nums)):
    a = nums[i-2]
    b = nums[i-1]
    c = nums[i]
    treh = [i for i in [a, b, c] if len(str(abs(i))) == 3]
    if len(treh) >= 2:
        if a+b+c >= mini:
            reses.append(a+b+c)
        
print(len(reses), min(reses))
