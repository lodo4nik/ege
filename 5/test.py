from itertools import product
cnt = 0
answ_cnt = 0
s = sorted("ЕГЭ")
for pos, word in enumerate(product(s, repeat=5), start=1):
    cnt = 0
    w = ''.join(word)
    if w.count("ГГ") == 0:
        for i in w:
            if i in "ЕЭ":
                cnt+=1
        if cnt >= 3:
            if pos % 2 == 0:
                answ_cnt += 1
print(answ_cnt)