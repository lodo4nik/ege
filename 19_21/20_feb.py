# def f(a, b, step=0):
#     s = a+b
#     if s >= 59 and step == 1: return 1
#     if s >= 59 and step < 1 or s < 59 and step == 1: return 0
#     step += 1
#     games = [f(a+1, b, step), f(a*2, b, step), f(a, b+1, step), f(a, b*2, step)]
#     if step % 2 != 0:
#         return any(games)
#     else: return any(games)
#
# for i in range(2, 54):
#     if f(5, i) == 1:
#         print(i)

# def f(a, b, step=0):
#     s = a+b
#     if s >= 59 and step == 3: return 1
#     if s >= 59 and step < 3 or s < 59 and step == 3: return 0
#     step += 1
#     games = [f(a+1, b, step), f(a*2, b, step), f(a, b+1, step), f(a, b*2, step)]
#     if step % 2 != 0:
#         return any(games)
#     else: return all(games)
#
# for i in range(2, 54):
#     if f(5, i) == 1:
#         print(i)

def f(a, b, step=0):
    s = a+b
    if s >= 59 and (step == 2 or step == 4): return 1
    if s >= 59 and step < 4 or s < 59 and step == 4: return 0
    step += 1
    games = [f(a+1, b, step), f(a*2, b, step), f(a, b+1, step), f(a, b*2, step)]
    if step % 2 == 0:
        return any(games)
    else: return all(games)

def f1(a, b, step=0):
    s = a+b
    if s >= 59 and step == 2: return 1
    if s >= 59 and step < 2 or s < 59 and step == 2: return 0
    step += 1
    games = [f1(a+1, b, step), f1(a*2, b, step), f1(a, b+1, step), f1(a, b*2, step)]
    if step % 2 == 0:
        return any(games)
    else: return all(games)

for i in range(2, 53):
    if f(5, i) == 1 and f1(5, i) != 1:
        print(i)