cords1 = input().split()
cords = sorted([int(x) for x in cords1])
n = len(cords)

dists = []
for i in range(n - 1):
    dists.append(cords[i + 1] - cords[i])
dp = [0] * n
dp[1] = dists[0]
if n > 2:
    dp[2] = dists[0] + dists[1]
    for i in range(3, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + dists[i - 1]

print(dp[n - 1])