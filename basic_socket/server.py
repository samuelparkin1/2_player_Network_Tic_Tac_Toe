import socket 
import pickle
from game import *

class Server():
    print ("Server online....")

    def __init__ (self):
        self.server_ip = socket.gethostbyname(socket.gethostname()) #automatically gets ip address of computer
        self.port = 50053
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Prevents changing port number 
        self.server_socket.bind((self.server_ip, self.port))
        self.play = User()
        self.symbol = "x"
        print(self.server_socket.getsockname())
 
    def connect(self):
        print ("Server listening for client....")
        self.server_socket.listen(2)
        self.conn, self.addr = self.server_socket.accept()
        print ('Connected by', self.addr)
    
    def receive (self):
        while True:
            data = self.conn.recv(4096)
            received_msg = pickle.loads(data)
            if received_msg:
                return (received_msg)
            break
                
    def send (self, message):
        # Pickle the object and send it to the server
        sending_msg = pickle.dumps(message)
        self.conn.send(sending_msg)
        print ('Data Sent to client')

server = Server()
server.connect()
server.play.turn = False
Game().play(server)