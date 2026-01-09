# def f(n):
#     if n <= 2:
#         return n
#     if n > 2:
#         return f(n-1) + f(n-2)
#
# print(f(10))


# def f(n):
#     if n == 1:
#         return 3
#     if n == 2:
#         return 1
#     if n > 2:
#         return 68 + f(n-2)
#
# print(f(13))

# def f(n):
#     if n == 1:
#         return 1
#     if n > 1 and n % 2 == 0:
#         return n*n + f(n-1)
#     if n > 1 and n % 2 != 0:
#         return f(n-1) + 2*f(n-2)
#
# print(f(25))

# def f(n):
#     if n == 1:
#         return 6
#     if n == 2:
#         return 8
#     if n == 3:
#         return 100
#     if n > 3:
#         return 3 + 2 * f(n-2)
#
# print(f(13))

# def f(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 3
#     if n > 1:
#         return f(n-1) - f(n-2) + 2*n
#
# print(f(15))

# def f(n):
#     if n == 1:
#         return 1
#     if n >= 2:
#         return f(n-1) + 3*g(n-1)
#
# def g(n):
#     if n == 1:
#         return 1
#     if n >= 2:
#         return f(n-1) - 2*g(n-1)
#
# print(f(18))


# def f(n):
#     if n == 1:
#         return 1
#     if n >= 2:
#         return f(n-1) - 2*g(n-1)
#
# def g(n):
#     if n == 1:
#         return 1
#     if n >= 2:
#         return f(n-1) + 2*g(n-1)
#
# print(g(21))

# from functools import *
# import sys
# sys.setrecursionlimit(100000)
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n + f(n-1)
#
# print(f(2023) - f(2019))
#
#
#
# from functools import *
#
# @lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return n + f(n-1)
#
# for n in range(1, 2023+1, 1): # заранее просчитываем самое большое число и закидываем в кеш
#     f(n)
#
# print(f(2023) - f(2019))


# from functools import *
# import sys
# sys.setrecursionlimit(100000)
# @lru_cache(None)
# def f(n):
#     if n <= 1:
#         return 1
#     if n > 1:
#         return n * f(n-2)
#
# print(f(2023) / f(2019))


# from functools import *
# import sys
# sys.setrecursionlimit(100000)
# @lru_cache(None)
# def f(n):
#     if n <= 2:
#         return 1
#     if n > 2:
#         return n + f(n-2)
#
# print(f(2023) + f(2020))


# from functools import *
# import sys
# sys.setrecursionlimit(100000)
# @lru_cache(None)
# def f(n):
#     if n >= 2025:
#         return n
#     if n < 2025:
#         return n + f(n+2)

# print(f(2022) - f(2023))