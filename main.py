import asyncio, websockets, json, time, threading
import netcututils as nc
from scapy.all import *

import asyncio, websockets, json, time, threading
import netcututils as nc
from scapy.all import *
import controller as c
import sys

async def process(websocket, path):
    async for message in websocket:
        print(message)
        request = json.loads(message)
        print(request)
        val = c.controller(request)
        if val is not None:
            await websocket.send(val)


if len(sys.argv) > 1:
    if sys.argv[1] == "-s" or sys.argv[1] =="--server":
        asyncio.get_event_loop().run_until_complete(
        websockets.serve(process, 'localhost', 8765))
        asyncio.get_event_loop().run_forever()
    else:
        print("unknow argument, launching on standalone")
        while True:
            input = input().lower().split()
            if input[0] == "quit" :
                break;
            else:
                val = c.controller(input)
                if val is not None:
                    print(val)
            del input
else:
    while True:
        input = input().lower().split()
        if input[0] == "quit" :
            break;
        else:
            val = c.controller(input)
            if val is not None:
                print(val)
        del input