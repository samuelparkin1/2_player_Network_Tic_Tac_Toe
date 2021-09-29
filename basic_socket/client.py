import socket 
import pickle
from game import *

class Client():
    def __init__(self):
        self.server = socket.gethostbyname(socket.gethostname()) #automatically gets ip address of computer
        self.port = 50053
        self.addr = (self.server, self.port)        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.addr)
        self.play = User()
        self.symbol = "o"
        
    def connect(self):
        pass

    def send(self, message):
        data_string = pickle.dumps(message)
        self.client.send(data_string)


    def receive(self):
        while True:
            data = self.client.recv(4096)
            print ("recv")
            received_msg = pickle.loads(data)
            if received_msg:
                print (received_msg)
                print ('Data received from Server')
                return (received_msg)
            break

client = Client()
client.connect()
client.play.turn = True
Game().play(client)