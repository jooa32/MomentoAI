import boto3 #boto3 is AWS SDK for python, which allows python deveopers to write the software that makes use of services like Amazon S3 and Amazon EC2
from google.cloud import storage # GCP blob storage

class ServiceMigrationTool:
    def __init__(self) -> None:
        pass
        
    def migrate_bucket(self, aws_bucket_name, gcp_bucket_name):
        
    s3 = boto3.resource('s3')

    # Create an S3 client
    s3_client = boto3.client('s3')
    # print(s3_client)

    # List buckets using the client to verify it works
    s3_resource = boto3.resource('s3')
    print(s3_resource)

