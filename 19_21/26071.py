def f(a, step=0):
    if a >= 125 and (step == 2 or step == 4): return 1
    if a >= 125 and step < 4 or a < 125 and step == 4: return 0
    step += 1
    if a % 2 == 0:
        games = [f(a*2, step), f(a+2, step)]
    if a % 2 != 0:
        games = [f(a*2, step), f(a+4, step)]

    if step % 2 == 0:
        return any(games)
    else: return all(games)


def f1(a, step=0):
    if a >= 125 and step == 2: return 1
    if a >= 125 and step < 2 or a < 125 and step == 2: return 0
    step += 1
    if a % 2 == 0:
        games = [f1(a*2, step), f1(a+2, step)]
    if a % 2 != 0:
        games = [f1(a*2, step), f1(a+4, step)]

    if step % 2 == 0:
        return any(games)
    else: return all(games)


for i in range(1, 125):
    if f(i) == 1 and f1(i) != 1:
        print(i)
