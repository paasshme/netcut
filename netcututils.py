import nmap
from scapy.all import *

# Return IP & Mac of every connected device (Root might be useful be not necessary)
def nmap_scan(target_ip= '192.168.0.0/24'):
    nmScan=nmap.PortScanner()
    print("scan begin")
    devices = nmScan.scan(target_ip,"1")
    print(devices)
    ips=[]
    for ip in devices["scan"]:
        ips.append(ip)

    print(ips)
    return ips

# Return IP & Mac of every connected client (Need root)
def arp_scan(target_ip = '192.168.0.0/24'):
    
    # IP Address for the destination
    # create ARP packet
    arp = ARP(pdst=target_ip)
    # create the Ether broadcast packet
    # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
    ether = Ether(dst='ff:ff:ff:ff:ff:ff')
    # stack them
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    # a list of clients, we will fill this in the upcoming loop
    clients = []

    for sent, received in result:
        # for each response, append ip and mac address to `clients` list
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    # print clients
    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))

    return clients


def sniffing(src, dst):
    def editPkg(pkg):
        pkg.src = src
        pkg.dst = dst
        pkg.show
        print(pkg.show)
        # send(pkg)

    # sniff(prn=editPkg, filter="src " + src)
    sniff(prn=editPkg)

# if __name__=='__main__':
    # sniffing("1.1.1.1", "0.0.0.0")
def craft_arp_spoof(target_ip, gateway_ip):
    return ARP(op = 2, psrc = gateway_ip, pdst = target_ip)

if __name__=='__main__':
    # arp_scan('192.168.2.0/24')
    arp_scan()
    arp_spoof("aaa")
