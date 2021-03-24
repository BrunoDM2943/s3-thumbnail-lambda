from PIL import Image
from urllib.parse import unquote_plus
import boto3

s3 = boto3.client('s3')

def generate_thumb(image_path, thumb_path):
    with Image.open(image_path) as image:
        print(image.format, f"{image.size}x{image.mode}")
        image.thumbnail(tuple(x / 2 for x in image.size))
        image.save(thumb_path)

def lambda_handle(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        
        fileName = key.split("/")[1]
        download_path = '/tmp/{}'.format(fileName) 
        upload_path = '/tmp/thumb_{}'.format(fileName)

        print("Bucket Name: {} Key {}".format(bucket, key))
        s3.download_file(bucket, key, download_path)
        generate_thumb(download_path, upload_path)
        s3.upload_file(upload_path, bucket, 'thumbs/{}'.format(fileName))