try:
    import socket 
    import pickle
    from game import *
except ModuleNotFoundError as import_error:
    print (import_error)
    exit()



class Server():

    def __init__ (self):
        self.server_ip = socket.gethostbyname(socket.gethostname()) #automatically gets ip address of computer
        self.port = 50053
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Prevents changing port number 
        self.socket.bind((self.server_ip, self.port))
        self.info = []
        self.username = "P1" #(input("whats your players name? "))
        self.opponent = []
        self.symbol = "x"
        print(f"The server ip address:\n{self.server_ip}")
 
    def connect(self):
        print ("Waiting for client to join....")
        self.socket.listen(2)
        self.conn, self.addr = self.socket.accept()
        self.opponent = self.receive()
        self.send(self.username)
        
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

server = Server()
server.connect()
server.info =User(server.opponent)
server.info.turn = False
Game().play(server)
