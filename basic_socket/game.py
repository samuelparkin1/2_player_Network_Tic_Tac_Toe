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
                    print ("\nSorry, that position has been taken.\n")
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
    
    def draw(self, moves,):

        if any (item in self.options for item in moves):
            return False
        else:
            print ("The game was a draw")
            return True

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
    def __init__(self, opponent ):
        self.moves = ["x","x","3","o","o","6","7","8","9"]
        #self.moves = ["1","2","3","4","5","6","7","8","9"]
        self.opponent = opponent
        self.opponent_symbol = []
        self.turn = []

    def out_going_message(self, symbol):
        moves = self.moves
        return (symbol, moves)

class Game ():

    connected = True

    def play (self, player):
        self.player = player
        while self.connected == True:
            try:
                self.game_play = True
                while self.game_play:
                    os.system('cls||clear')
                    Board(self.player.info.moves).grid()
                    if self.player.info.turn:
                        Tic_Tac_Toe().user_select(self.player.info.moves, self.player.symbol)
                        self.player.send(self.player.info.out_going_message(self.player.symbol))
                        self.player.info.turn = False
                        os.system('cls||clear')
                        Board(self.player.info.moves).grid()
                        if Tic_Tac_Toe().win_check(self.player.info.moves, self.player.symbol, self.player.username) or Tic_Tac_Toe().draw(self.player.info.moves):
                            
                            if Tic_Tac_Toe().replay():
                                self.player.info = User(self.player.info.opponent) 
                                self.game_play = False                    
                            else:
                                self.player.socket.close()
                                self.connected = False
                                break
                        
                    else:
                        print (f"Waiting for {self.player.info.opponent} to make a move.")
                        self.player.info.opponent_symbol, self.player.info.moves = self.player.receive()
                        os.system('cls||clear')
                        Board(self.player.info.moves).grid()
                        if Tic_Tac_Toe().win_check(self.player.info.moves, self.player.info.opponent_symbol, self.player.opponent) or Tic_Tac_Toe().draw(self.player.info.moves):
                                
                            if Tic_Tac_Toe().replay():
                                self.player.info = User(self.player.info.opponent) 
                                self.game_play = False                    
                            else:
                                self.player.socket.close()
                                self.connected = False
                                break    
                        self.player.info.turn = True

            except EOFError:
                self.player.socket.close()
                print (input ("Looks like the other player has disconnected. Press Enter to end game"))
                self.connected = False


