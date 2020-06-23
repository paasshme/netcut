import asyncio, websockets, json, time
import netcututils as nc
#Return an array with every IP of connected devices (on local network)

state = False
async def echo(websocket, path):
    
    async for message in websocket:
        
        request = json.loads(message)
        if request[0] == "nmap_scan":
            await websocket.send(json.dumps(nc.nmap_scan()))
        elif request[0] == "arp_scan":
            await websocket.send(json.dumps(nc.arp_scan()))
        elif request[0] == "arp_spoof":
            state = True
            async while state:
                time.sleep(0.5)
                print("yo")
        elif request[0] == "stop":
            state = False
            print("re")
        else:
            await websocket.send("this request doesn't exist")

        
        # print(f'1 , {request[0]} \n')
        # print(f'2 , {request[1]}')
       
        # await websocket.send(json.dumps(nmap_scan()))
        print("scan end")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()


