import socket
import pickle
class Client():
    def __init__(self):        
        self.header = 64
        self.port = 5055
        self.format = 'utf-8'
        self.disconnect_message = "!DISCONNECT"
        self.server = socket.gethostbyname(socket.gethostname()) #automatically gets ip address of computer
        self.addr = (self.server, self.port)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.addr)

    def send_utf8(self,msg):
        message = msg.encode(self.format)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.format)
        send_length += b' ' * (self.header - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        print(self.client.recv(2048).decode(self.format))

    def send_pickle (self, msg):
        variable = msg
        # Pickle the object and send it to the server
        data_string = pickle.dumps(variable)
        self.client.send(data_string)

client1 = Client ()

while True:
    client1.send_pickle(input())
    #client1.send_pickle({1:"hi", 2: "there"})



