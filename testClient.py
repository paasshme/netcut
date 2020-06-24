import asyncio, json
import websockets

async def hello(uri):
	async with websockets.connect(uri) as ws:
		await ws.send(json.dumps(("arp_scan",)))
		# await ws.send(json.dumps(("sniff", "192.168.0.11")))
		a=await ws.recv()
		print(a)
		# input("aa")	
		# await ws.send(json.dumps(("spoof_stop", "192.168.0.11")))
		# await ws.send(json.dumps(("sniff_stop", "192.168.0.11")))
		# print("sended")
		

asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8765'))
