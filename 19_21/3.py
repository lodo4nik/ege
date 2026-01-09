# https://education.yandex.ru/ege/inf/task/745a1abe-b282-4d35-8005-8cca2df7bcc2

def f(s, m):
    if s > 33: return m%2 == 0
    if m == 0: return 0
    h = [f(s+1, m-1), f(s+2, m-1), f(s+3, m-1), f(s*2, m-1)]
    return any(h) if m%2 != 0 else all(h)

print([s for s in range(1, 34) if f(s, 2)])
print([s for s in range(1, 34) if not f(s, 1) and f(s, 3)])
print([s for s in range(1, 34) if not f(s, 2) and f(s, 4)])