import asyncio, json
import websockets

async def hello(uri):
	async with websockets.connect(uri) as ws:
		await ws.send(json.dumps(("smart_sniff", "192.168.0.11")))
		print("sended")
		# a=await ws.recv()
		# print(a)

asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8765'))
