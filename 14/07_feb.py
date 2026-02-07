def to_32(x):
    k = 0
    while x:
        ost = x % 32
        if ost > 9:
            k += 1
        x //= 32
    return k


s = 2**2048 + 32**102 - 8*(4**128)
print(to_32(s))