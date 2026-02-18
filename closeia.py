def query(n):
    secret_T = 150
    secret_t = 30
    return secret_T + n * secret_t

q1 = query(4)
q2 = query(2)
t = q2-q1
T = q1-t

print(T, t)