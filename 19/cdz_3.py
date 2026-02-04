def f(a, step=0):
    if a >= 40 and step == 2: return 1
    if a >= 40 and step < 2 or a < 40 and step == 2: return 0
    step += 1
    games = [f(a+1, step), f(a+2, step), f(a*2, step)]
    if step % 2 == 0:
        return any(games)
    else:
        return any(games)

for i in range(1, 40):
    if f(i) == 1:
        print(i)