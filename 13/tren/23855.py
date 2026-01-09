from ipaddress import *

net = ip_network("172.95.116.174/255.255.192.0", strict=False)

for adr in net:
    print(adr+1)
    exit()