from ipaddress import *

net = ip_network("150.122.11.21/255.255.254.0", strict=False)
print(net[1])

print(bin(int(net[1])).count("1"))