from itertools import product

s = "АБКЛМОР"

k = 0
ws = []
for s1 in product(s, repeat=4):
    f = 0
    ws.append(''.join(s1))

for i in range(0, len(ws)):
    if ws[i] == "БЛОК":
        print(i, ws[i])
    if ws[i] == "КРАБ":
        print(i, ws[i])
