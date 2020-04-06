# Real-time Road Traffic Surveillance using Cloud

![FlowChart](FlowChart.png) 

## Ivy
Ivy is an open source video-based vehicle counting system which employs several computer vision techniques to detect, track and count vehicles in a traffic scene.

![Output](Output.png) 

## Requirements
- Python 3
- AWS account

## AWS Services to be setup:
- EC2
- Lambda
- Media Convert
- S3
- Cloudfront

## Setup
- Clone this repo 
- Install the dependencies in _requirements.txt_ `pip install -r requirements.txt`.
- Install detector YOLO's dependencies where necessary [ivy_demo_data.zip](https://drive.google.com/open?    id=1JtEhWlfk1CiUEFsrTQHQa0VkTi3IKbze) and unzip its contents in the [data directory](/data). It contains Yolo model's weight.

| Detector | Description | Dependencies |
|---|---|---|
| `yolo` | Perform detection using models created with the YOLO (You Only Look Once) neural net. https://pjreddie.com/darknet/yolo/ | |


## Run(Only for testing ivy model locally)
- Create a _.env_ file (based on _.env.example_) in the project's root directory and edit as appropriate.
- Run `python -m  main`.

## Run(Cloud vehicle counting)
- Create instances mentioned above. 
- Replace bucket names with your bucket name.
- Change the path of the local video file.
- Start the server by running `python Run.py`.
- Start the consumer on the cloud by running `python consumer.py`.
- Start the producer on the local by running `python producer.py`.
- Run the codes in Lamda to setup the file conversion and log writting.
- Setup the web application by running the HTML on the web browser.
- Refresh the webapp to see the output.



