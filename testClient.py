import asyncio, json
import websockets

async def hello(uri):
	async with websockets.connect(uri) as ws:
		await ws.send(json.dumps(("arp_spoof", "192.168.0.11")))
		await ws.send(json.dumps(("sniff", "192.168.0.11")))
		input("input")
		await ws.send(json.dumps(("spoof_stop", "192.168.0.11")))
		await ws.send(json.dumps(("sniff_stop", "192.168.0.11")))
		print("sended")
		# a=await ws.recv()
		# print(a)

asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8765'))
