import asyncio, json
import websockets

async def hello(uri):
	async with websockets.connect(uri) as ws:
		await ws.send(json.dumps(("nmap_scan",)))
		print("sended")
		a=await ws.recv()
		print(a)

asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8765'))
