class Service:
    def __init__(self, name, host):
        self.name = name
        self.host = host
        self.running = False

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

def migrate_service(service, new_host):
    service.migrate(new_host)

if __name__ == "__main__":
    # Create a service instance
    my_service = Service(name="TestService", host="HostA")

    # Start the service
    my_service.start()

    # Migrate the service to a new host
    migrate_service(my_service, "HostB")

    # Ensure the service is running on the new host
    if my_service.host == "HostB" and my_service.running:
        print("Service migration successful.")
    else:
        print("Service migration failed.")
