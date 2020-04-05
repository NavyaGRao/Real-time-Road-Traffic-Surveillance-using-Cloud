import glob
import json
import os
import uuid
import boto3
import datetime
import random
import urllib.parse
from time import sleep

from botocore.client import ClientError

def handler(event, context):

    assetID = str(uuid.uuid4())
    sourceS3Bucket = event['Records'][0]['s3']['bucket']['name']
    sourceS3Key = event['Records'][0]['s3']['object']['key']
    sourceS3 = 's3://'+ 'your-bucket-name'+ '/' + 'output.avi'
    sourceS3Basename = sourceS3
    #sourceS3Basename = os.path.splitext(os.path.basename(sourceS3))[0]
    #destinationS3 = 's3://' + os.environ['DestinationBucket']
    destinationS3 = 's3://' +'out-put-test'
    destinationS3basename = destinationS3
    #destinationS3basename = os.path.splitext(os.path.basename(destinationS3))[0]
    mediaConvertRole = 'MediaConvert_Default_Role'
    #os.environ['MediaConvertRole']
    region = 'us-east-1'
    #os.environ['AWS_DEFAULT_REGION']
    statusCode = 200
    body = {}

    # Use MediaConvert SDK UserMetadata to tag jobs with the assetID 
    # Events from MediaConvert will have the assetID in UserMedata
    jobMetadata = {'assetID': assetID}

    print (json.dumps(event))

    try:
        # Job settings are in the lambda zip file in the current working directory
        with open('job.json') as json_data:
            jobSettings = json.load(json_data)
            print(jobSettings)

        # get the account-specific mediaconvert endpoint for this region
        mc_client = boto3.client('mediaconvert', region_name=region)
        endpoints = mc_client.describe_endpoints()

        # add the account-specific endpoint to the client session 
        client = boto3.client('mediaconvert', region_name=region, endpoint_url=endpoints['Endpoints'][0]['Url'], verify=False)



        
        # Create MediaConvert client
        #mediaconvert_client = boto3.client('mediaconvert', endpoint_url='https://abcd1234.mediaconvert.us-west-2.amazonaws.com')
        
        # Load job.json from disk and store as Python object: job_object
        with open("job.json", "r") as jsonfile:
            job_object = json.load(jsonfile)
        
        # Create MediaConvert job by unpacking the arguments from job_object. The job object contains the required parameters 
        # for create_job. Pass these to create_job using Python's ** argument unpacking syntax.
        client.create_job(**job_object)
        
                
       

    except Exception as e:
        print ('Exception: %s' % e)
        #print(statusCode = 500)
        raise

    finally:
        return {
            'statusCode': statusCode,
            'body': json.dumps(body),
            'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}
        }
