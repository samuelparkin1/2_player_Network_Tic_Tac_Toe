import socket 
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

    def connect(self):
        print ("Server listening for client....")
        self.server_socket.listen(2)
        self.conn, self.addr = self.server_socket.accept()
        print ('Connected by', self.addr)
    
    def receive (self):
            data = self.conn.recv(4096)
            received_msg = pickle.loads(data)
            if received_msg:
                print (received_msg)
                print ('Data received from client')
        
    def send (self, message):
        # Pickle the object and send it to the server
        sending_msg = pickle.dumps(message)
        self.conn.send(sending_msg)
        print ('Data Sent to client')


class Board():
    def __init__(self, positions):
        self.positions = positions
        
    def grid(self,):
        print ('-------')
        print ('|' + self.positions[0] + '|' + self.positions[1] +'|' + self.positions[2] + '|')
        print ('-------')
        print ('|' + self.positions[3] + '|' + self.positions[4] +'|' + self.positions[5] + '|')
        print ('-------')
        print ('|' + self.positions[6] + '|' + self.positions[7] +'|' + self.positions[8] + '|')
        print ('-------')

    def clear(self):
        os.system('cls||clear')

class Symbol():
    def __init__(self, symbol):
        self.symbol = symbol[0]

class Game():
    def __init__(self):
        self.username = "sam" #(input("whats your players name?"))
        self.symbol = self.username[0].capitalize
        self.opponent = []
        self.moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.options = ("1","2","3","4","5","6","7","8","9")


    
       
    def user_select(self):
        
        while True:
            user_input = input("what position?")
            if user_input in self.options:
                if str(user_input) in self.moves:
                    self.moves[int(user_input)-1] = str(self.symbol())
                    break
                else:
                    print ("choose again")
            else:
                print ("choose again1")

    def win_check (self):
        if (
            (self.moves[0] == self.moves[1] == self.moves[2] == self.symbol()) or 
            (self.moves[3] == self.moves[4] == self.moves[5] == self.symbol()) or 
            (self.moves[6] == self.moves[7] == self.moves[8] == self.symbol()) or 
            (self.moves[0] == self.moves[3] == self.moves[6] == self.symbol()) or
            (self.moves[1] == self.moves[4] == self.moves[8] == self.symbol()) or 
            (self.moves[2] == self.moves[5] == self.moves[8] == self.symbol()) or
            (self.moves[0] == self.moves[4] == self.moves[8] == self.symbol()) or 
            (self.moves[2] == self.moves[4] == self.moves[6] == self.symbol())
        ):
            print ("win_check")
            return True
        else:
            return False
  

game1 = Game()
Board(game1.moves).grid()
while True:
    game1.user_select()
    #os.system('cls||clear')
    if game1.win_check():
        Board(game1.moves).grid()
        print ('you win')
        break
    Board(game1.moves).grid()


#board = Board()
# board.positions= [game1.symbol, "2", " ", " ", " ", " ", " ", " ", " "]
# print(board.positions)
# board.clear()
# board.grid()






