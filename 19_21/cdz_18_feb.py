# def f(a, b, step=0):
#     s = a+b
#     if 63 <= s <= 74 and step == 2: return 1
#     if 63 <= s <= 74 and step < 2 or s < 63 and step == 2: return 0
#     if s > 74 and step == 2: return 0
#     if s > 74 and step != 2: return 1
#     step += 1
#     games = [f(a+2, b, step), f(a*2, b, step), f(a, b+2, step), f(a, b*2, step)]
#     if step % 2 == 0: return any(games)
#     else: return any(games)
#
# print("- 19 -")
# for i in range(1, 100):
#     if f(15, i) == 1:
#         print(i)

def f(a, b, step=0):
    s = a+b
    if 63 <= s <= 74 and step == 1: return 0
    if 63 <= s <= 74 and step == 3: return 1
    if 63 <= s <= 74 and step < 3 or s < 63 and step == 3: return 0
    if s > 74 and step == 3: return 0
    if s > 74 and step != 3: return 1
    step += 1
    games = [f(a+2, b, step), f(a*2, b, step), f(a, b+2, step), f(a, b*2, step)]
    if step % 2 != 0: return any(games)
    else: return all(games)

print("- 19 -")
for i in range(1, 48):
    if f(15, i) == 1:
        print(i)