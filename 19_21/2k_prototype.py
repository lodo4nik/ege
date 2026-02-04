def f(a, b, step):
    s = a+b
    if s >= 159 and step == 2: #победа вани
        return True
    if s < 159 and step == 2 or s >= 159 and step==2: # проигрыш вани и победа пети
        return False

    step += 1
    return f(a+1, b, step) or f(a+3, b, step) or f(a*2, b, step) or f(a, b+1, step) or f(a, b+3, step) or f(a, b*2, step)

for b in range(1, 131):
    if f(7, b, 0):
        print(b)