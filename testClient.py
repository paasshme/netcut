import asyncio, json
import websockets

async def hello(uri):
	async with websockets.connect(uri) as ws:
		await ws.send(json.dumps(("arp_spoof", "yo", "salut")))
		input("input")
		await ws.send(json.dumps(("stop", "yo", "salut")))
		print("sended")
		a=await ws.recv()
		print(a)

asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8765'))
