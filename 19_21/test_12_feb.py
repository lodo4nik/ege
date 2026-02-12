from math import *

def f(a, step=0):
    if a <= 23 and step == 2: return 1
    if a <= 23 and step < 2 or a > 23 and step == 2: return 0
    step += 1
    if a % 2 != 0:
        games = [f(a-5, step), f(a-7, step), f(floor(a/2), step)]
    else:
        games = [f(a - 5, step), f(a - 7, step), f(ceil(a / 2), step)]
    if step % 2 == 0: return any(games)
    else: return all(games)

print("- 19 -")
for i in range(30, 100):
    if f(i) == 1:
        print(i)




def g(a, step=0):
    if a <= 23 and step == 3: return 1
    if a <= 23 and step < 3 or a > 23 and step == 3: return 0
    step += 1
    if a % 2 != 0:
        games = [g(a-5, step), g(a-7, step), g(floor(a/2), step)]
    else:
        games = [g(a - 5, step), g(a - 7, step), g(ceil(a / 2), step)]
    if step % 2 != 0: return any(games)
    else: return all(games)

print("- 20 -")
for i in range(30, 100):
    if g(i) == 1:
        print(i)




def f1(a, step=0):
    if a <= 23 and (step == 2 or step == 4): return 1
    if a <= 23 and step < 4 or a > 23 and step == 4: return 0
    step += 1
    if a % 2 != 0:
        games = [f1(a-5, step), f1(a-7, step), f1(floor(a/2), step)]
    else:
        games = [f1(a - 5, step), f1(a - 7, step), f1(ceil(a / 2), step)]
    if step % 2 == 0: return any(games)
    else: return all(games)

def f2(a, step=0):
    if a <= 23 and step == 2: return 1
    if a <= 23 and step < 2 or a > 23 and step == 2: return 0
    step += 1
    if a % 2 != 0:
        games = [f2(a-5, step), f2(a-7, step), f2(floor(a/2), step)]
    else:
        games = [f2(a - 5, step), f2(a - 7, step), f2(ceil(a / 2), step)]
    if step % 2 == 0: return any(games)
    else: return all(games)

print("- 21 -")
for i in range(30, 1000):
    if f1(i) == 1 and f2(i) != 1:
        print(i)