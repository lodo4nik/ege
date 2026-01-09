from ipaddress import *

adrs = []
net = ip_network("191.128.66.83/255.192.0.0", strict=False)
for adr in net:
    adrs.append(adr)

print(adrs[-2])
print(net[-2])