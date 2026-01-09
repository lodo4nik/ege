f = open("26_17537.txt")
n, m, k = (int(i) for i in f.readline().split())

min_row = [m+1]*(k+1)

for i in range(n):
    r, s = [int(x) for x in f.readline().split()]
    min_row[s] = min(min_row[s], r)

ans1 = 0
for i in range(1, k):
    ans1 = max(ans1, min(min_row[i]-1, min_row[i+1]-1))
print(ans1)