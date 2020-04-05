import asyncio
import websockets
import numpy
import cv2
import base64
import sys

import json

vidcap = cv2.VideoCapture('./ivy/data/videos/crop1.mp4')


def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

async def produce(message: str, host: str, port: int) -> None:
	async with websockets.connect(f"ws://{host}:{port}") as ws:
		await ws.send(message)
		await ws.recv()

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	success,image = vidcap.read()
	count = 0

	while success:
		
		success,image = vidcap.read()
		if(success == False):
			loop.run_until_complete(produce(message="Done", host='35.182.254.11', port=9696))
			exit()
		image = rescale_frame(image, percent=75)
		cv2.imwrite('frame.jpg',image)
		
		with open("frame.jpg", "rb") as image_file:
			encoded_string = base64.b64encode(image_file.read())
		print(sys.getsizeof(encoded_string))
		loop.run_until_complete(produce(message=encoded_string, host='35.182.254.11', port=9696))
		encoded_string = 0



#15.223.54.179
