def zamena(x):
    s = [int(i) for i in str(x)]
    s1 = list(reversed([s[-2], s[-1]]))
    s[-2] = s1[-2]
    s[-1] = s1[-1]
    return int(''.join([str(i) for i in s]))

def f(x, end):
    if x == end: return 1
    if x > end: return 0
    s = [int(i) for i in str(x)]
    if s[-2] < s[-1]:
        return f(x+1, end)+f(zamena(x), end)
    else:
        return f(x+1, end)
    
print(f(101, 154))
