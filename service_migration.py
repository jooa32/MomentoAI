import boto3 # type: ignore
from google.cloud import storage
import os

# Set up AWS S3 client
s3_client = boto3.client('s3', aws_access_key_id='YOUR_AWS_ACCESS_KEY', aws_secret_access_key='YOUR_AWS_SECRET_KEY', region_name='YOUR_AWS_REGION')
source_bucket = 'your-source-bucket-name'

# Set up GCS client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/gcp-credentials.json'
storage_client = storage.Client()
destination_bucket = storage_client.bucket('your-destination-bucket-name')

def migrate_file(s3_client, source_bucket, destination_bucket, key):
    # Download the file from S3
    s3_client.download_file(source_bucket, key, key)
    print(f'Downloaded {key} from S3')

    # Upload the file to GCS
    blob = destination_bucket.blob(key)
    blob.upload_from_filename(key)
    print(f'Uploaded {key} to GCS')

    # Clean up the local file
    os.remove(key)
    print(f'Removed local file {key}')

def main():
    # List objects in the source S3 bucket
    # testing 
    objects = s3_client.list_objects_v2(Bucket=source_bucket)
    if 'Contents' in objects:
        for obj in objects['Contents']:
            key = obj['Key']
            try:
                migrate_file(s3_client, source_bucket, destination_bucket, key)
            except Exception as e:
                print(f'Failed to migrate {key}: {e}')
    else:
        print(f'No objects found in {source_bucket}')

if __name__ == '__main__':
    main()