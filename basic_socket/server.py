import socket 
import threading
import pickle
import os

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

    def received_messages(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
        while True:
            data = conn.recv(4096)
            received_msg = pickle.loads(data)
            if received_msg:
                print (received_msg)
                print ('Data received from client')
                break

        conn.close()
    
    def sending_messages(self, message):
        # Pickle the object and send it to the server
        sending_msg = pickle.dumps(message)
        self.conn.send(sending_msg)
        print ('Data Sent to client')     

    def connect(self):
        print ("Server listening for client....")
        self.server_socket.listen(2)
        while True:
            conn, addr = self.server_socket.accept()
            thread = threading.Thread(target=self.received_messages, args=(conn, addr))
            thread.start()
            print(f"players connected {threading.activeCount() - 1}")



server1 = Server()
server1.connect()
