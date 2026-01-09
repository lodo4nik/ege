with open('ttt.txt', 'r') as f:
    file = f.readlines()
    c = 0
    m_dv = -1000000000000
    file = [i for i in file if i != '\n']
    file = [int(i.strip()) for i in file]
    for i in range(len(file) - 1):
        if (abs(file[i]) % 23 == 0 and abs(file[i + 1]) % 29 != 0) or \
                (abs(file[i]) % 29 != 0 and abs(file[i + 1]) % 23 == 0):
            c += 1
            if file[i] + file[i + 1] > m_dv:
                m_dv = file[i] + file[i + 1]
    print(c, m_dv)
