# def f(s1, s2, step):
#     if s1 + s2 <= 200 and step == 2: return True
#     if (s1 + s2 >= 200 and step < 2) or (s1 + s2 < 200 and step == 2): return False
#
#     if step % 2 == 0:
#         return f(s1-3, s2-4, step+1) and f(s1-8, s2//2, step+1) and f(s1 // 2 + s1 % 2, s2 - 10, step+1)
#     if step % 2 != 0:
#         return f(s1-3, s2-4, step+1) or f(s1-8, s2//2, step+1) or f(s1 // 2 + s1 % 2, s2 - 10, step+1)
#
# for s2 in range(100, 10000):
#     if f(110, s2, 0):
#         print(s2)


def f(a,b,m):
    if a + b <= 200: return m % 2 == 0
    if m == 0: return 0
    h = [f(a - 3,b - 4,m - 1), f(a - 8,b // 2,m - 1),f(a // 2 + a % 2,b - 10,m - 1)]
    return any(h) if m % 2 else all(h)


print('19', [i for i in range(100,1000) if f(110,i,2)])
print('20', [i for i in range(100,1000) if f(110,i,3) and (not f(110,i,1))])
print('21', [i for i in range(100,1000) if f(110,i,4) and (not f(110,i,2))])