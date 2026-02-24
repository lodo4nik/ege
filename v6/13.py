from ipaddress import *
net = ip_network("173.142.100.17/255.255.254.0", strict=False)
print(net[-2])
