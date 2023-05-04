import boto3
import os

BUCKET_NAME = "mv-videos"

s3 = boto3.client("s3")
video_file = './videos/video_test.mp4'

directory = 'videos'

def sendToS3():
    for filename in os.listdir(directory):
        video_path = os.path.join(directory, filename)
        # checking if it is a file
        if not os.path.isfile(video_file):
            print('NOT A File')
        # # Create an S3 client and upload the video file
        with open(video_path, 'rb') as f:
            s3.upload_fileobj(f, BUCKET_NAME, filename)

        # Set the S3 object permissions to public-read
        s3.put_object_acl(ACL='public-read', Bucket=BUCKET_NAME, Key=filename)

        # Generate the public URL for the uploaded video
        s3_url = f'https://{BUCKET_NAME}.s3.amazonaws.com/{filename}'
        print(f'Video URL: {s3_url}')