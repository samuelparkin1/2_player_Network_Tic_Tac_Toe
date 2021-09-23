import socket, pickle
import game
import os

class Client():
    def __init__(self):
        self.server = socket.gethostbyname(socket.gethostname()) #automatically gets ip address of computer
        self.port = 50053
        self.addr = (self.server, self.port)        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.addr)

    def send(self, message):
        data_string = pickle.dumps(message)
        self.client.send(data_string)
        print ('Data Sent to Server')

    def receive(self):
        data = self.client.recv(4096)
        data_variable = pickle.loads(data)
        print (data_variable)
        print ('Data received from Server')

        
'''
    def comms(self):
        while True:
            variable = input()
            data_string = pickle.dumps(variable)
            self.client.send(data_string)
            print ('Data Sent to Server')
            data = self.client.recv(40096)
            data_variable = pickle.loads(data)
            print (data_variable)
            print ('Data received from Server')
'''
        
client1 = Client()
client1.send(input("what is your message?\n"))
client1.receive()
