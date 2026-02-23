from ipaddress import *
net = ip_network("10.77.87.21/255.255.255.240", strict=False)
for ip in net:
    ip1 = [bin(int(oc))[2:].zfill(8) for oc in str(ip).split(".")]
    if ip1[3].count("1") <= ip1[0].count("1"):
        print(ip)
