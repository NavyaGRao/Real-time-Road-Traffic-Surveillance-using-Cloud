import json
import urllib.parse
import boto3
print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:

        Acl = s3.get_object_acl(Bucket=bucket, Key=key)
        Aclnow= s3.put_object_acl(Bucket=bucket, Key=key ,ACL='public-read-write')
        
        return Aclnow
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
