# N19 -----------------------------------------------------------------------------

def f2(a, step=0):
    if a <= 23 and step == 2: return 1
    if a <= 23 and step < 2 or a > 23 and step == 2: return 0
    step += 1
    if step % 2 == 0:
        games = [f2(a-5, step), f2(a-7, step), f2(a // 2, step)]
        return any(games)
    else:
        games = [f2(a - 5, step), f2(a - 7, step), f2(a // 2, step)]
        return all(games)

print("- 19 -")
for i in range(30, 100):
    if f2(i) == 1:
        print(i)

# N20 -----------------------------------------------------------------------------

def f3(a, step=0):
    if a <= 23 and step == 3: return 1
    if a <= 23 and step < 3 or a > 23 and step == 3: return 0
    step += 1
    if step % 2 == 1:
        games = [f3(a-5, step), f3(a-7, step), f3(a // 2, step)]
        return any(games)
    else:
        games = [f3(a - 5, step), f3(a - 7, step), f3(a // 2, step)]
        return all(games)

print("- 20 -")
for i in range(30, 100):
    if f3(i) == 1:
        print(i)

# N21 -----------------------------------------------------------------------------

def f24(a, step=0):
    if a <= 23 and (step == 2 or step == 4): return 1
    if a <= 23 and step < 4 or a > 23 and step == 4: return 0
    step += 1
    if step % 2 == 0:
        games = [f24(a-5, step), f24(a-7, step), f24(a // 2, step)]
        return any(games)
    else:
        games = [f24(a - 5, step), f24(a - 7, step), f24(a // 2, step)]
        return all(games)

def f4(a, step=0):
    if a <= 23 and step == 4: return 1
    if a <= 23 and step < 4 or a > 23 and step == 4: return 0
    step += 1
    if step % 2 == 0:
        games = [f4(a-5, step), f4(a-7, step), f4(a // 2, step)]
        return any(games)
    else:
        games = [f4(a - 5, step), f4(a - 7, step), f4(a // 2, step)]
        return all(games)

print("- 21 -")
for i in range(30, 1000):
    if f24(i) == 1 and f4(i) != 1 and f2(i) != 1: # победа В1 или В2, но не В1 и не В2 по отдельности!
        print(i)