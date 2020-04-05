import asyncio
import websockets
from server import Server


server = Server()
start_server = websockets.serve(server.ws_handler,'0.0.0.0', 9696)
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()