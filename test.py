import boto3
from google.cloud import compute_v1

class Service:
    def __init__(self, name, host):
        self.name = name
        self.host = host
        self.running = False
        self.ec2 = boto3.client('ec2', region_name='us-west-2')  # Replace 'us-west-2' with your desired AWS region


    def start(self):
        self.running = True
        print(f"Service {self.name} started on {self.host}.")

    def stop(self):
        self.running = False
        print(f"Service {self.name} stopped on {self.host}.")

    def migrate(self, new_host):
        self.stop()
        print(f"Migrating service {self.name} from {self.host} to {new_host}.")
        self.host = new_host
        self.start()

class AWSService(Service):
    def __init__(self, name, instance_id):
        super().__init__(name, f"AWS instance {instance_id}")
        self.instance_id = instance_id
        self.ec2 = boto3.client('ec2')


    def start(self):
        super().start()
        self.ec2.start_instances(InstanceIds=[self.instance_id])
        print(f"AWS instance {self.instance_id} started.")

    def stop(self):
        super().stop()
        self.ec2.stop_isntance(InstanceIds=[self.instance_id])
        print(f"AWS instance {self.instance_id} stopped.")

    def migrate(self, new_instance_id):
        self.stop()
        print(f"Migrating AWS service {self.name} from {self.instance_id} to {new_instance_id}.")
        self.instance_id = new_instance_id
        self.host = f"AWS instance {new_instance_id}"
        self.start()

class GCPService(Service):
    def __init__(self,name,instance_name, zone):
        super().__init__(name, f"GCP instance {instance_name}")
        self.instance_name = instance_name
        self.zone = zone
        self.client = compute_v1.InstancesClient()

    def start(self):
        super().start()
        # Start the GCP instance
        self.client.start(project='YOUR_PROJECT_ID', zone=self.zone, instance=self.instance_name)
        print(f"GCP instance {self.instance_name} started.")

    def stop(self):
        super().stop()
        # Stop the GCP instance
        self.client.stop(project='YOUR_PROJECT_ID', zone=self.zone, instance=self.instance_name)
        print(f"GCP instance {self.instance_name} stopped.")

    def migrate(self, new_instance_name, new_zone):
        self.stop()
        print(f"Migrating GCP service {self.name} from {self.instance_name} to {new_instance_name}.")
        self.instance_name = new_instance_name
        self.zone = new_zone
        self.host = f"GCP instance {new_instance_name}"
        self.start()

def migrate_service(service, new_host, new_zone=None):
    # check the type of service and handle migration accordingly
    if isinstance(service, AWSService):
        service.migrate(new_host)
    elif isinstance(service, GCPService) and new_zone is not None:
        service.migrate(new_host, new_zone)
    else:
        raise ValueError("Unsupported service type or missing new_zone for GCPService")


if __name__ == "__main__":
    # Create a service instance
    aws_service = AWSService(name="TestServiceAWS", instance_id="i-0abcd1234efgh5678")

    # Start the AWS service
    aws_service.start()

    # Migrate the AWS service to a new instance
    migrate_service(aws_service, "i-0hijklmno9pqrstuv")

    # Ensure the AWS service is running on the new instance
    if aws_service.host == "AWS instance i-0hijklmno9pqrstuv" and aws_service.running:
        print("AWS service migration successful.")
    else:
        print("AWS service migration failed.")

    # Create GCP service instance
    gcp_service = GCPService(name="TestServiceGCP", instance_name="instance-1", zone="us-central1-a")

    # Start the GCP service
    gcp_service.start()

    # Migrate the GCP service to a new instance and zone
    migrate_service(gcp_service, "instance-2", "us-central1-b")

    # Ensure the GCP service is running on the new instance
    if gcp_service.host == "GCP instance instance-2" and gcp_service.running:
        print("GCP service migration successful.")
    else:
        print("GCP service migration failed.")