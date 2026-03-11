from ipaddress import *

for mask in range(1, 33):
    net = ip_network(f'231.150.114.158/{mask}', strict = False)
    net1 = str(net).split("/")
    if net1[0] == "231.150.114.128":
        print(net)
