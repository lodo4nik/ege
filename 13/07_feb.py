from ipaddress import *
net = ip_network("192.168.32.160/255.255.255.240", strict=False)
k= 0
for ip in net:
    s = (bin(int(ip))[2:].zfill(32))
    if s.count("0") > 21:
        k+=1
print(k)