import scapy.all as scapy

def scan_network(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

print("Scanning network...")
clients = scan_network("192.168.0.1/24")
print("IP\t\tMAC Address\n-----------------------------------------")
for client in clients:
    print(client["ip"] + "\t" + client["mac"])

