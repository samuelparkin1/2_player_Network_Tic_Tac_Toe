import socket 
import threading
import pickle

class Server():
    print ("Server online....")
    def __init__ (self):
        self.server_ip = socket.gethostbyname(socket.gethostname()) #automatically gets ip address of computer
        self.port = 50053
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Prevents changing port number 
        self.server_socket.bind((self.server_ip, self.port))
        self.conn = ()
        self.addr = ()
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
                print (received_msg)
                print ('Data received from client')
                break
        
    def send (self, message):
        # Pickle the object and send it to the server
        sending_msg = pickle.dumps(message)
        self.conn.send(sending_msg)
        print ('Data Sent to client')

server1 = Server()
server1.connect()
server1.receive()
server1.send(input("what is your message?\n"))