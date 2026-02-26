def f(a, b, step=0):
    s = a+b
    if s >= 150 and (step == 2 or step == 4): return 1
    if s >= 150 and step < 4 or s < 150 and step == 4: return 0
    step+=1
    games = [f(a+2, b, step), f(a*3, b, step), f(a, b+2, step), f(a, b*3, step)]
    if step % 2 == 0:
        return any(games)
    else:
        return all(games)

def f1(a, b, step=0):
    s = a+b
    if s >= 150 and step == 2: return 1
    if s >= 150 and step < 2 or s < 150 and step == 2: return 0
    step+=1
    games = [f1(a+2, b, step), f1(a*3, b, step), f1(a, b+2, step), f1(a, b*3, step)]
    if step % 2 == 0:
        return any(games)
    else:
        return all(games)

for i in range(1, 134):
    if f(16, i) == 1 and f1(16, i) != 1:
        print(i)
