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
        


    def connect(self):
        print ("Server listening for client....")
        self.server_socket.listen(1)
        conn, addr = self.server_socket.accept()
        print ('Connected by', addr)

        while True:
            data = conn.recv(4096)
            data_variable = pickle.loads(data)
            #conn.close()
            print (data_variable)
            print ('Data received from client')

            variable = input()
            # Pickle the object and send it to the server
            data_string = pickle.dumps(variable)
            conn.send(data_string)
            #s.close()
            print ('Data Sent to client')

server1 = Server()
server1.connect() 