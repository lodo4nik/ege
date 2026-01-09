# a = []
# for n in range(1, 10000):
#     r = bin(n)[2:]
#     if n % 5 == 0:
#         r = r + r[-2] + r[-1]
#     else:
#         ost = bin(n % 5 * 5)[2:]
#         r = r + ost
#
#     if int(r, 2) >= 377:
#         a.append(int(r, 2))
#
# print(min(a))

s = '2' * 894
c = 0
while '222' in s or '666' in s:
    if '222' in s:
        s = s.replace('222', '6', 1)
    else:
        s = s.replace('666', '2', 1)
        c += 3
print(c)
