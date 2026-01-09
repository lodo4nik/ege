# def f(n):
#     if n > 2:
#         return 5 + f(n-2)
#     if n == 1:
#         return 6
#     if n == 2:
#         return 8
#
# print(f(4))


def f(n, k):
    if n == 114:

        return 1
    if n > 114:
        return 0

    return f(n+1, k + f'{n + 1} ') + (n-2)

print(f(3), '')