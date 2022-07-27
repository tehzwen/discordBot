
class Server:
    def __init__(self, details: dict) -> None:
        self.ip = details['ip']
        self.name = details['name']

    # returns the command to ping this server
    def ping(self) -> str:
        return f"ping -c 1 {self.ip}"
