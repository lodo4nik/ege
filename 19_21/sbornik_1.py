def f(a, step=0):
    if a<=60 and (step == 2 or step == 4): return 1
    if a <= 60 and step < 4 or a > 60 and step == 4: return 0
    step+=1
    games = [f(a-3, step), f(a-5, step), f(a//4, step)]
    if step % 2 == 0:
        return any(games)
    else:
        return all(games)
    
def f1(a, step=0):
    if a<=60 and step == 2: return 1
    if a <= 60 and step < 2 or a > 60 and step == 2: return 0
    step+=1
    games = [f1(a-3, step), f1(a-5, step), f1(a//4, step)]
    if step % 2 == 0:
        return any(games)
    else:
        return all(games)
def f2(a, step=0):
    if a<=60 and step == 4: return 1
    if a <= 60 and step < 4 or a > 60 and step == 4: return 0
    step+=1
    games = [f2(a-3, step), f2(a-5, step), f2(a//4, step)]
    if step % 2 == 0:
        return any(games)
    else:
        return all(games)

for i in range(61, 1000):
    if f(i) == 1 and f1(i) == 0 and f2(i) == 0:
        print(i)
