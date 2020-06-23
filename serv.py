import asyncio, websockets, nmap, jsonify

async def echo(websocket, path):
    async for message in websocket:
        print(message,path)
        nmScan=nmap.PortScanner()
        print("scan begin")
        devices = nmScan.scan("192.168.0.1/24","1")
        ips=[]
        for ip in devices["scan"]:
            ips.append(ip)
        print(ips)
        await websocket.send(ips)
        print("scan end")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
