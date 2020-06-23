import asyncio
import websockets

async def hello(uri):
	async with websockets.connect(uri) as ws:
		await ws.send("salut salut salut")
		await ws.recv()

asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8765'))
