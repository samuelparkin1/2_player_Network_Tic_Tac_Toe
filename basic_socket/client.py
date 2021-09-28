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

        while True:
            data = self.client.recv(4096)
            print ("recv")
            received_msg = pickle.loads(data)
            if received_msg:
                print (received_msg)
                print ('Data received from Server')
                return (received_msg)
            break
             

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
        self.options = ("1","2","3","4","5","6","7","8","9")
    
    def incoming_message(self):
        message = self.connection.receive()
        print (message)
        # self.opponent = message[0], 
        # self.moves = message[1]

    def out_going_message(self):

        opponent = self.username
        moves = self.moves
        Server().send("hey")
        Server().send(opponent, moves)    
       
    def user_select(self,moves, symbol):
        self.moves = moves
        self.symbol = symbol
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

    def win_check (self,moves,symbol):

        if (
            (moves[0] == moves[1] == moves[2] == symbol()) or 
            (moves[3] == moves[4] == moves[5] == symbol()) or 
            (moves[6] == moves[7] == moves[8] == symbol()) or 
            (moves[0] == moves[3] == moves[6] == symbol()) or
            (moves[1] == moves[4] == moves[8] == symbol()) or 
            (moves[2] == moves[5] == moves[8] == symbol()) or
            (moves[0] == moves[4] == moves[8] == symbol()) or 
            (moves[2] == moves[4] == moves[6] == symbol())
        ):
            print ("win_check")
            return True
        else:
            return False

class User():
    def __init__(self):
        self.username = "sam" #(input("whats your players name?"))
        self.symbol = self.username[0].capitalize
        self.moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.opponent = []
        self.opponent_symbol = []
        self.turn = True

    def out_going_message(self):
        opponent = self.username
        moves = self.moves
        symbol = self.symbol
        return (opponent, symbol, moves)
        
while True:
    client1 = Client()
    new_user = User()
    game_play = True
    while game_play:
        Board(new_user.moves).grid()
        if new_user.turn:
            Game().user_select(new_user.moves, new_user.symbol)
            if Game().win_check(new_user.moves,new_user.symbol) == True:
                game_play = False
            client1.send(new_user.out_going_message())
            new_user.turn = False
            print (new_user.turn) 
        else:
            print (new_user.turn)
            new_user.opponent, new_user.opponent_symbol, new_user.moves = client1.receive()
            if Game().win_check(new_user.moves, new_user.opponent_symbol) == True:
                game_play = False       
            print (new_user.moves)
            new_user.turn = True


# Board(game1.moves).grid()
# while True:
#     game1.user_select()
#     #os.system('cls||clear')
#     if game1.win_check():
#         Board(game1.moves).grid()
#         print ('you win')
#         break
#     Board(game1.moves).grid()
        
#client1 = Client()
#client1.send(input("what is your message?\n"))
#client1.receive()
