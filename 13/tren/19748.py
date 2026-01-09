from ipaddress import *

for mask in range(32, -1, -1):
    net1 = ip_network(f"157.220.185.237/{mask}", strict=False)
    net2 = ip_network(f"157.220.184.230/{mask}", strict=False)

    if net1 == net2:
        cnt = 0
        for addr in net1:
            if bin(int(addr)).count("1") == 15:
                cnt += 1
        print(cnt)
        exit()