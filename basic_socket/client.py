import socket, pickle
class ProcessData:
    def __init__(self, data= 'ABCDEFGHIJK'):
        self.data = data
    def __str__(self): return self.data

HOST = socket.gethostbyname(socket.gethostname()) #automatically gets ip address of computer
PORT = 50005
# Create a socket connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    # Create an instance of ProcessData() to send to server.
    variable = input()
    # Pickle the object and send it to the server
    data_string = pickle.dumps(variable)

    s.send(data_string)

    #s.close()
    print ('Data Sent to Server')
    data = s.recv(40096)
    data_variable = pickle.loads(data)
    #conn.close()
    print (data_variable)
    print ('Data received from Server')






'''
import socket, pickle
import game

class Client():
    def __init__(self):
        self.server = socket.gethostbyname(socket.gethostname()) #automatically gets ip address of computer
        self.port = 50006
        self.addr = (self.server, self.port)        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.addr)

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
        
client1 = Client()
client1.comms()
'''