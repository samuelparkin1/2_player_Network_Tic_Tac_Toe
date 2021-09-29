try:
    import socket 
    import pickle
    from game import *
except ModuleNotFoundError as import_error:
    print (import_error)
    exit()

class Client():
    def __init__(self):
        self.server = input("Please enter servers IP address\n") #automatically gets ip address of computer
        self.port = 50053
        self.addr = (self.server, self.port)        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.info = []
        self.username = (input("whats your players name? "))
        self.opponent= []
        self.symbol = "o"
        
    def connect(self):        
        self.socket.connect(self.addr)
        self.send(self.username)
        self.opponent = self.receive()



    def send(self, message):
        data_string = pickle.dumps(message)
        self.socket.send(data_string)


    def receive(self):
        while True:
            data = self.socket.recv(4096)
            received_msg = pickle.loads(data)
            if received_msg:
                return (received_msg)
            break

client = Client()
try:
    client.connect()
except ConnectionRefusedError:
    print ("Server not connected...")
    exit()
client.info = User(client.opponent)
client.info.turn = True
Game().play(client)
