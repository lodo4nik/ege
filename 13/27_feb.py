from ipaddress import *
net = ip_network("172.16.168.0/255.255.248.0", strict=False)
k = 0
for ip in net:
    if bin(int(ip)).count("1") % 5 != 0:
        k += 1
print(k)
