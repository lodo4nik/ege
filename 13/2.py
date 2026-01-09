# https://education.yandex.ru/ege/inf/task/c76b728d-6c5e-40c8-a212-acafbcdcbd0c

from ipaddress import *
net = ip_network("192.168.160.0/255.255.224.0", strict=False)
mask_bits = bin(int(net.netmask)).count('1')

cnt = 0

for addr in net:
    if bin(int(addr)).count('1') == mask_bits:
        cnt+=1

print(cnt)