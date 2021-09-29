import os

class Board():
    def __init__(self, positions):
        self.positions = positions
        
    def grid(self,):
        print ('-------------')
        print ('| ' + self.positions[6] + ' | ' + self.positions[7] +' | ' + self.positions[8] + ' | ')
        print ('-------------')
        print ('| ' + self.positions[3] + ' | ' + self.positions[4] +' | ' + self.positions[5] + ' | ')
        print ('-------------')
        print ('| ' + self.positions[0] + ' | ' + self.positions[1] +' | ' + self.positions[2] + ' | ')
        print ('-------------')

    def clear(self):
        os.system('cls||clear')

class Symbol():
    def __init__(self, symbol):
        self.symbol = symbol[0]

class Tic_Tac_Toe():
    def __init__(self):
        self.options = ("1","2","3","4","5","6","7","8","9")
        
    def user_select(self,moves, symbol):
        self.moves = moves
        self.symbol = symbol
        while True:
            user_input = input(f"Using the corresponding numbers,\nselect a position for your marker? ('{self.symbol}') ")
            if user_input in self.options:
                if str(user_input) in self.moves:
                    self.moves[int(user_input)-1] = str(self.symbol)
                    break
                else:
                    print ("Sorry, that position has been taken.")
            else:
                print ("Sorry but that is an invalid input.")

    def win_check (self,moves,symbol,player):
        if (
            (moves[0] == moves[1] == moves[2] == symbol) or 
            (moves[3] == moves[4] == moves[5] == symbol) or 
            (moves[6] == moves[7] == moves[8] == symbol) or 
            (moves[0] == moves[3] == moves[6] == symbol) or
            (moves[1] == moves[4] == moves[8] == symbol) or 
            (moves[2] == moves[5] == moves[8] == symbol) or
            (moves[0] == moves[4] == moves[8] == symbol) or 
            (moves[2] == moves[4] == moves[6] == symbol)
        ):
            print (f"{player} has Won the game" )
            return True
        else:
            return False

    def replay (self):
        while True:
            play_again = input("Would you like to play agin? ").capitalize
            print (play_again())
            if play_again()[0] == "Y":
                return True
            if play_again()[0] == "N":
                return False
            else:
                print("Please enter Yes/No ")

class User():
    def __init__(self):
        self.username = "sam" #(input("whats your players name?"))
        #self.symbol = "x"
        self.moves = ["1","2","3","4","5","6","7","8","9"]
        self.opponent = []
        self.opponent_symbol = []
        self.turn = []

    def out_going_message(self, symbol):
        opponent = self.username
        moves = self.moves
        return (opponent, symbol, moves)

class Game ():

    connected = True
    def play (self, player):
        self.player = player
        while self.connected == True:     
            self.game_play = True
            while self.game_play:
                os.system('cls||clear')
                Board(self.player.play.moves).grid()
                if self.player.play.turn:
                    Tic_Tac_Toe().user_select(self.player.play.moves, self.player.symbol)
                    self.player.send(self.player.play.out_going_message(self.player.symbol))
                    self.player.play.turn = False
                    os.system('cls||clear')
                    Board(self.player.play.moves).grid()
                    if Tic_Tac_Toe().win_check(self.player.play.moves, self.player.symbol, self.player.play.opponent):
                        if Tic_Tac_Toe().replay():
                            self.player.play = User() 
                            self.game_play = False                    
                        else:
                            self.connected = False
                            break
                    
                else:
                    print ("Waiting for other player to make a move.")
                    self.player.play.opponent, self.player.play.opponent_symbol, self.player.play.moves = self.player.receive()
                    os.system('cls||clear')
                    Board(self.player.play.moves).grid()            
                    if Tic_Tac_Toe().win_check(self.player.play.moves, self.player.play.opponent_symbol, self.player.play.opponent):
                        if Tic_Tac_Toe().replay():
                            self.player.play = User() 
                            self.game_play = False                    
                        else:
                            self.connected = False
                            break    
                    self.player.play.turn = True
