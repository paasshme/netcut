import asyncio, websockets, nmap, json

async def echo(websocket, path):
    async for message in websocket:
        if (int(message) == 1)
        print(message)
       
        await websocket.send(json.dumps(ips))
        print("scan end")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()


#Return an array with every IP of connected devices (on local network)
async def nmap_scan():
    nmScan=nmap.PortScanner()
    print("scan begin")
    devices = nmScan.scan("192.168.0.1/24","1")
    ips=[]
    for ip in devices["scan"]:
        ips.append(ip)
    
    return ips