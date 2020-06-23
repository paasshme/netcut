import asyncio, websockets, json
import netcututils as nc
#Return an array with every IP of connected devices (on local network)


async def echo(websocket, path):
    async for message in websocket:
        # if (int(message) == 1)
        print(message)
        nc.magic()
       
        await websocket.send(json.dumps(nc.nmap_scan()))
        print("scan end")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()


