from ipaddress import *

net = ip_network("202.71.92.91/255.255.192.0", strict=False)

for addr in net:
    fracted = str(addr).split(".")
    oks = 0
    for i in range(len(fracted)):
        if int(fracted[i]) % 2 != 0:
            oks += 1
    if oks == 2 and addr != net.broadcast_address:
        print(addr)