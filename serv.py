import asyncio, websockets, nmap, json

#Return an array with every IP of connected devices (on local network)
def nmap_scan():
    nmScan=nmap.PortScanner()
    print("scan begin")
    devices = nmScan.scan("192.168.0.1/24","1")
    ips=[]
    for ip in devices["scan"]:
        ips.append(ip)
    
    return ips

async def echo(websocket, path):
    async for message in websocket:
        request = json.loads(message)
        if request[0] == "scan":
            
        elif request[0] == "block":

        
        print(f'1 , {request[0]} \n')
        print(f'2 , {request[1]}')
       
        # await websocket.send(json.dumps(nmap_scan()))
        print("scan end")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()


