# 19
# def f(s, step):
#     if s >= 129 and step == 2:
#         return True
#     if (s >= 129 and step < 2) or (s < 129 and step == 2):
#         return False
#     if step % 2 == 0:
#         return f(s+1, step+1) and f(s*2, step + 1)
#     if step % 2 != 0:
#         return f(s+1, step+1) or f(s*2, step + 1)


# 20
def f(s, step):
    if s >= 129 and (step == 4 or step == 2):
        return True
    if (s >= 129 and step < 4) or (s < 129 and step == 4):
        return False
    if step % 2 == 0:
        return f(s+1, step+1) and f(s*2, step + 1)
    if step % 2 != 0:
        return f(s+1, step+1) or f(s*2, step + 1)


for s in range(1, 129):
    if f(s, 0):
        print(s)