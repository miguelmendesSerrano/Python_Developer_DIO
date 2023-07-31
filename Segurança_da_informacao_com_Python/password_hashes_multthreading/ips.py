""" Working with Ips """

import ipaddress

ip = '192.168.0.1'

address_ip = ipaddress.ip_address(ip)
print(address_ip + 100)
print(address_ip + 2000)
print('=' * 14)

ip_network = '192.168.0.0/24'

network_address = ipaddress.ip_network(ip_network, strict=False)
print(network_address)
print('=' * 14)

for ips in network_address:
    print(ips)
