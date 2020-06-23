import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(message,path)
        nmScan=nmap.PortScanner()
	    devices = nmScan.scan("192.168.0.1/23","1")

	    ips=[]
	    for ip in devices["scan"]:
	    	ips.append(ip)

    
	    return jsonify(ips)
            await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
