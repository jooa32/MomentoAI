# service migration - migrate a simple web app from one EC2 instance 
# to another using an automated approach?

# AWS SDK for python - to integrate python application, lib, or script with AWS service
import boto3

# initialize Boto3
ec2_client = boto3.client('ec2', region_name='us-west-2')
route53_client = boto3.client('route53', region_name='us-west-2')

def migrate_service():
    """migrate a service from one EC2 instance to anohter"""
    print("print service migrate")

    # Get user input
    instance_id = input("Enter Instance ID: ")
    # source_instance_id = input("Enter Source Instance ID: ")
    # key_name = input("Enter Key Name: ")
    # security_group_ids = input("Enter Security Group IDs (comma-separated): ").split(',')
    # subnet_id = input("Enter Subnet ID: ")
    # hosted_zone_id = input("Enter Hosted Zone ID: ")
    # record_set_name = input("Enter Record Set Name: ")

    

def main():
    migrate_service()
    # print("hello world")

if __name__ == "__main__":
    main()