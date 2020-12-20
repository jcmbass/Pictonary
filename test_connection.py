import socket
import json

class Network:
    def __init__(self, name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.name = name
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            self.client.sendall(self.name.encode())
            return json.loads(self.client.recv(2048))
        except Exception as e:
            self.disconnect(e)
    
    def send_str(self, data):
        """
        docstring
        """
        try:
            self.client.connect(self.addr)
            self.client.sendall(self.name.encode())
            return json.loads(self.client.recv(2048))
        except Exception as e:
            self.disconnect(e)

    def send(self, data):
        """
        Loops so that all bytes that are recieved and correctly sended
        :data: Json
        :returns: None
        """
        try:
            self.client.send(json.dumps(data).encode())
            d = ""  # variable for storing all bytes that can be recieved.
            while 1:
                last = self.client.recv(1024).decode()
                d += last
                try:
                    if d.count(".") == 1:
                        break
                except:
                    pass
            try:
                if d[-1] == ".":
                    d = d[:-1]
            except:
                pass
            keys = [key for key in data.keys()]
            return json.loads(d)[str(keys[0])]
        except socket.error as e:
            self.disconnect(e)

    def disconnect(self, msg):
        """
        Ensures that the socket is cleanly disconnected if an exception is raised.
        """
        print("[EXCEPTION] Disconnected from server:", msg)
        self.client.close()

n = Network("Tech with Yosu")
print(n.send({0:["hello"]}))