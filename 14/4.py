s = 625**90 + 125**120 - 5*25

nums = []
while s > 0:
    ost = s%25
    if ost % 2 == 0:
        nums.append(ost)
    s //= 25

print(sum(nums))