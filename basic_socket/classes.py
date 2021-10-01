import os
import socket
import pickle


class Comms():

    def __init__(self, server_ip, symbol):
        # automatically gets ip address of computer
        self.server_ip = server_ip
        self.port = 50053
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Prevents changing port number
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.addr = (self.server_ip, self.port)
        self.username = input("whats your players name? ").capitalize()
        self.symbol = symbol
        self.game_info = []

    def send(self, message):
        # Pickle the object and send it to the server
        sending_msg = pickle.dumps(message)
        self.conn.send(sending_msg)

    def receive(self):
        while True:
            data = self.conn.recv(4096)
            received_msg = pickle.loads(data)
            if received_msg:
                return (received_msg)
            break


class Board():
    def __init__(self, positions):
        self.positions = positions

    def grid(self,):
        print ('-------------')
        print ('| ' + self.positions[6] + ' | ' + self.positions[7] + ' | ' + self.positions[8] + ' | ')
        print ('-------------')
        print ('| ' + self.positions[3] + ' | ' + self.positions[4] + ' | ' + self.positions[5] + ' | ')
        print ('-------------')
        print ('| ' + self.positions[0] + ' | ' + self.positions[1] + ' | ' + self.positions[2] + ' | ')
        print ('-------------')

    def clear(self):
        os.system('cls||clear')


class Tic_Tac_Toe():
    def __init__(self):
        self.options = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

    def user_select(self, moves, symbol):
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

    def win_check(self, moves, symbol, player):
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
            print (f"{player} won the game")
            return True
        else:
            return False

    def draw(self, moves,):

        if any(item in self.options for item in moves):
            return False
        else:
            print ("The game was a draw")
            return True

    def replay(self):
        while True:
            play_again = input("Would you like to play agin? ").capitalize
            print (play_again())
            if play_again()[0] == "Y":
                return True
            if play_again()[0] == "N":
                return False
            else:
                print("Please enter Yes/No ")


class User_info():
    def __init__(self, opponent):
        self.moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.opponent = opponent
        self.opponent_symbol = []
        self.turn = []

    def out_going_message(self, symbol):
        moves = self.moves
        return (symbol, moves)


class Game ():

    connected = True

    def play(self, player):
        self.player = player
        while self.connected:
            try:
                self.game_play = True
                while self.game_play:
                    os.system('cls||clear')
                    Board(player.game_info.moves).grid()
                    if player.game_info.turn:
                        Tic_Tac_Toe().user_select(player.game_info.moves, player.symbol)
                        player.send(player.game_info.out_going_message(player.symbol))
                        player.game_info.turn = False
                        os.system('cls||clear')
                        Board(player.game_info.moves).grid()
                        if Tic_Tac_Toe().win_check(player.game_info.moves, player.symbol, "You have") or Tic_Tac_Toe().draw(player.game_info.moves):

                            if Tic_Tac_Toe().replay():
                                player.game_info = User_info(player.game_info.opponent)
                                self.game_play = False
                            else:
                                player.socket.close()
                                self.connected = False
                                break

                    else:
                        print (f"Waiting for {player.game_info.opponent} to make a move.")
                        player.game_info.opponent_symbol, player.game_info.moves = player.receive()
                        os.system('cls||clear')
                        Board(player.game_info.moves).grid()
                        if Tic_Tac_Toe().win_check(player.game_info.moves, player.game_info.opponent_symbol, f"{player.opponent} has") or Tic_Tac_Toe().draw(player.game_info.moves):

                            if Tic_Tac_Toe().replay():
                                player.game_info = User_info(player.game_info.opponent)
                                self.game_play = False
                            else:
                                player.socket.close()
                                self.connected = False
                                break
                        player.game_info.turn = True

            except EOFError:
                player.socket.close()
                print (input(f"Looks like {player.opponent} has disconnected. Press Enter to end game"))
                self.connected = False


class Asci_art():
    print("""
 _______________  _________  _____  __________  ____
/_  __/  _/ ___/ /_  __/ _ |/ ___/ /_  __/ __ \/ __/
 / / _/ // /__    / / / __ / /__    / / / /_/ / _/  
/_/ /___/\___/   /_/ /_/ |_\___/   /_/  \____/___/  
""")
