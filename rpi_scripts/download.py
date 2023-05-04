import boto3
import os

# set the S3 bucket name and the directory in the bucket where the MP4 files are stored
bucket_name = 'mv-videos'
directory = ''

# set the local directory to download the MP4 files to
local_dir = './video_out'

# create the local directory if it does not exist
os.makedirs(local_dir, exist_ok=True)

# create a new S3 client
s3 = boto3.client('s3')

# get a list of all the objects in the directory
objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=directory)["Contents"]

# # loop through the objects and download each MP4 file
for obj in objects:
    # get the object key (i.e. the filename) for the current object
    key = obj['Key']
    
    # check if the object is an MP4 file
    if key.endswith('.mp4'):
        # create a filename for the local copy of the MP4 file
        filename = key.split('/')[-1]
        
        # download the MP4 file from the S3 bucket to the current directory
        s3.download_file(bucket_name, key, f'./{local_dir}/{filename}')
        
        print(f'Downloaded {filename} from S3 bucket {bucket_name}')