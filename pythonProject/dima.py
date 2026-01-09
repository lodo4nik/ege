# def f(s, m):
#     if s >= 42: return m % 2 == 0
#     if m == 0: return 0
#
#     h = [f(s+1, m-1), f(s+3, m-1), f(s*2, m-1)]
#     return any(h) if m % 2 != 0 else all(h)
#
# print(19, [s for s in range(1, 41, 1) if f(s, 2)])
# print(20, [s for s in range(1, 41, 1) if not f(s, 1) and f(s, 3)])
# print(21, [s for s in range(1, 41, 1) if not f(s, 2) and f(s, 4)])

c = 0
for i1 in '1357':
    for i2 in '012345678':
        for i3 in '012345678':
            for i4 in '012345678':
                for i5 in '0234568':
                    s = i1 + i2 + i3 + i4 + i5
                    if s.count('6') <= 1:
                        c += 1

print(c)
# 1 0 0 0
# 0 0 0 1

# 1 1 0 0 True False
# 1 1 0 1 False False


