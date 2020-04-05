

import asyncio
import logging
import websockets
from websockets import WebSocketClientProtocol
import json
import base64
import cv2
import os
from PIL import Image
import io


decoder = json.JSONDecoder()
count = 0
frame_array = []
fps = 20
pathOut = './data/videos/sample_traffic_scene.mp4'






logging.basicConfig(level = logging.INFO)
async def consumer_handler(websocket: WebSocketClientProtocol) -> None :
                async for message in websocket:
                                log_message(message)

                                #img = stringToRGB(message)
                                #cv2.imshow('m',img)



async def consume(hostname: str, port: int) -> None:
                websocket_resource_url = f"ws://{hostname}:{port}"
                async with websockets.connect(websocket_resource_url) as websocket:
                                await consumer_handler(websocket)


def log_message(message: str) -> None:
                #logging.info(f"Message: {message}")
                # decode the image and save locally
                size = (1440,810)
                if(message == "Done"):
                                out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
                                for i in range(len(frame_array)):
                                        # writing to a image array
                                        out.write(frame_array[i])
                                out.release()
                                call_main()

                global count
                count = count + 1
                print(count)
                name = "frame%d.jpg" % count
                with open(name, "wb") as image_file:
                                image_file.write(base64.b64decode(message))


                img = cv2.imread(name)
                height, width, layers = img.shape
                size = (width,height)

                #inserting the frames into an image array
                frame_array.append(img)

                if(len(frame_array) == 600):
                                out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
                                for i in range(len(frame_array)):
                                        # writing to a image array
                                        out.write(frame_array[i])
                                out.release()
                                call_main()


        #img = cv2.imread("image_received.jpg")
        #cv2.imshow('m',img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        #logging.info(f"Decoded: {img}")

def call_main():
                os.system("python3.6 -m main &")
                frame_array.clear()




if __name__ == '__main__':
                loop = asyncio.get_event_loop()
                loop.run_until_complete(consume(hostname="localhost", port=9696))
                loop.run_forever()






