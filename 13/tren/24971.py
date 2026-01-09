from ipaddress import *

net = ip_network("111.222.0.124/255.255.224.0", strict=False)

for addr in net:
    if (bin(int(addr)).count("1") * bin(int(addr)).count("0")) % 2 != 0:
        print(addr)