# def find_divs(x):
#     divs = []
#     for div in range(2, int(x**0.5)+1):
#         if x % div == 0:
#             divs.append(div)
#             divs.append(x//div)
#     return divs
#
# for n in range(500_000, 500_200):
#     prime_divs = [i for i in find_divs(n) if len(find_divs(i))==0]
#     if len(prime_divs) == 0:
#         r = 0
#     else:
#         r = sum(prime_divs)
#         if r > 2000 and str(r).endswith("7"):
#             print(n, r)


# def f(x, end):
#     if x > end or x == 15: return 0
#     if x == end: return 1
#     return f(x+2, end)+f(x*2, end)+f(x**3, end)
#
# print(f(3, 50)*f(50, 200))

#
# def f(x, end):
#     if x < end: return 0
#     if x == end: return 1
#     return f(x-1, end)+f(x//2, end)
#
# print(f(89, 30)*f(30, 7))

# from functools import lru_cache
#
# @lru_cache(None)
# def f(n):
#     if n < 4: return 3
#     if n > 3: return 3*f(n-3)
#
# for i in range(1, 3335): f(i)
#
# print(f(3333)/f(3300))

# def to_eleven(x):
#     k = 0
#     while x:
#         ost = x % 11
#         if ost == 0:
#             k+=1
#         x //= 11
#     return k
#
# for x in range(1, 3001):
#     n = 9*(11**210) + 8*(11**150)-x
#     if to_eleven(n) == 60:
#         print(x)

# from ipaddress import *
# k = 0
# net = ip_network("112.208.0.0/255.255.128.0", strict=False)
# for ip in net:
#     ip_b = bin(int(ip))
#     if ip_b.count("1") % 11 == 0:
#         k+=1
# print(k)

# from itertools import product
#
# s = "АЙЛМ"
# k = 0
# for w in product(s, repeat=5):
#     k += 1
#     w1 = ''.join(w)
#     if w1.count("М") <= 1 and w1.count("ЛЛ") == 0:
#         print(k, w1)

# def find_r(n):
#     r = bin(n)[2:]
#     if n % 3 == 0:
#         r = r + r[-3:]
#     else:
#         r = r + bin((n % 3) * 3)[2:]
#
#     return int(r, 2)
#
# for n in range(1, 100000):
#     r = find_r(n)
#     if r >= 200:
#         print(n)
#         exit()
#
# from itertools import product, permutations
#
# def f(a, b, c, d):
#     return (a <= b) and (b <= c) and (c <= d)
#
# for x1, x2 in product([0, 1], repeat=2):
#     t = (
#         (0, x1, 1, 0, 1),
#         (0, x2, 1, 0, 1),
#         (0, 1, 1, 1, 1)
#     )
#
#     if len(t) == len(set(t)):
#         for p in permutations("abcd", r=4):
#             if all(f(**dict(zip(p, line))) == line[-1] for line in t):
#                 print(*p)

# from math import *
#
# for n in range(1, 1000):
#     w = ceil(2783 * ceil(log(n, 2)) / 8)
#     if w*3_845_627 >= 11*1024*1024*1024:
#         print(n)
#         exit()


