from ipaddress import *
net = ip_network("235.86.56.0/255.255.248.0", strict=False)
k = 0
for ip in net:
    if bin(int(ip)).endswith("11"):
        k+=1

print(k)