import os
import socket
import pickle


class Comms():
    """ 
    Socket communication variables. 

    This class contains the varable needed for a socket connection.
    This class can be utilized by either the server or the client. 

    Args:
    Takes in the IP address of the server. 
    Sets the players symbol for the game. 
    Used to receive messages on the socket connection. 

    Returns: 
    Used to send messages over the socket connection.

    """


    def __init__(self, server_ip, symbol):
        # The IP address of teh server. 
        self.server_ip = server_ip

        # The port number for teh connection. 
        self.port = 50053

        # Creates an intance of a socket connect over IPV4 TCP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Prevents changing port number if the port number in in use. 
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Save the the IP address and port number to a single variable.  
        self.addr = (self.server_ip, self.port)

        # Asks the user to input their name. 
        self.username = input("whats your players name? ").capitalize()

        # Save the symbol of the user. This is used for during the play 
        # of the game.
        self.symbol = symbol

        # a varibale used to save teh users information during the play 
        # of the game. 
        self.game_info = []


    def send(self, message):
        """ 
        Sends message over the sockets connection. 

        This function is called when the user needs to send a message 
        over the socket connection.
        The message is transmitted as a pickle. 

        Args:
        Takes in the variables that needs to be sent. 

        Returns: None       
        """

        # the variable or object is converted to a pickle.
        sending_msg = pickle.dumps(message)

        #Sends the message over the socket connection.
        self.conn.send(sending_msg)

    def receive(self):
        """ 
        Receives message over the sockets connection.

        This function is called when the user needs to receive a message 
        from the socket connection.
        The message is received as a pickle and is converted back to a 
        variable or object.

        Args: None. 

        Returns: The message back to the user. 

        Raises:
        
        """
        while True:
            # Waits for the message to be received. 
            data = self.conn.recv(4096)

            # Connvert message from a pickle back to a variable or object. 
            received_msg = pickle.loads(data)

            # Once message has been received return the message.  
            if received_msg:

                return (received_msg)
            break


class Board():
    """ 
    Displays the board to the user.

    The Board class is used to take in the moves that have been made 
    and display the TIC TAC TOE board with those moves. 

    Args: Takes in the positions / moves of the game.

    Returns: None    
    """

    def __init__(self, positions):
        self.positions = positions

    def grid(self,):
        """ 
       Prints the board.

        Prints the TIC TAC TOE board with either the moves that have been made or the available spots.

        Args: Takes in the postions that have been made

        Returns: None.         
        """

        print ('-------------')
        print ('| ' + self.positions[6] + ' | ' + self.positions[7] + ' | ' + self.positions[8] + ' | ')
        print ('-------------')
        print ('| ' + self.positions[3] + ' | ' + self.positions[4] + ' | ' + self.positions[5] + ' | ')
        print ('-------------')
        print ('| ' + self.positions[0] + ' | ' + self.positions[1] + ' | ' + self.positions[2] + ' | ')
        print ('-------------')


class Tic_Tac_Toe():
    """ 
    TIC TAC TOE game functions. 

    This class contains the functions needed to play the game TIC TAC TOE.
    
    Args: 
    Each functions will call arguments that is needed for it to execute correctly. 

    Returns: 
    Each functions will return their own values. 
    """

    def __init__(self):
        
        # These options are referenced as allowable moves that the player can select during the game.   
        self.options = ("1", "2", "3", "4", "5", "6", "7", "8", "9")


    def user_select(self, moves, symbol):
        """ 
        For the player to select their move.

        This function is called when the player needs to select the move they wish to make. 
        
        Args:
        Takes in the moves that have been made and available spots on the board. 
        it then checks to wether the the selected move is available  

        Returns:
        update the moves that have been made and returns it to the user.
        
        """
        # take in the list of moves that have been made.
        self.moves = moves

        # Takes in the players symbol that is making a move. 
        self.symbol = symbol

        while True:
            # Aske the user to input their move. 
            user_input = input(f"Using the corresponding numbers,\nselect a position for your marker? ('{self.symbol}') ")

            # Check to see if the user has selected a move that is between 1-9 of the grid. 
            if user_input in self.options:

                # Checks to see if the user has selected a number that has already been taken.
                if str(user_input) in self.moves:

                    # updates the list of moves made with the position to user selected. 
                    # Replaces the number in the list with the players symbol.  
                    self.moves[int(user_input)-1] = str(self.symbol)
                    break
                else:
                    # Notifies user the they have selected a number that has already been taken 
                    print ("\nSorry, that position has been taken.\n")
            else:
                # notifies user they have not put in a valid move.
                print ("Sorry but that is an invalid input.")

    def win_check(self, moves, symbol, player):
        """ 
        Checks if the move has won the game.

        This will check to see if the move that has been made has won the game.

        Args:
        Takes in the list of moves, the players symbol and the players name. 

        Returns:
        If the player has won the game it will return a a True value and a message notifying the user of the win. 
        If no win was made it wil return a False value.        
        """
        # Will go though every possible winning move to check if the contain they all contain the players symbol. 
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
            # Prints message to user of a win of the game. 
            print (f"{player} won the game")

            # Returns a true value. 
            return True
        else:
            # Returns a False value.
            return False

    def draw(self, moves,):
        """ 
        Checks for a draw in te game. 

        This will check if there are any available spots left on the board, If not it wil call a draw of the game. 
        
        Args:
        Takes in the moves made by the players and move options.  

        Returns:
        Returns a False value is no draw was made.
        Returns a True value if a draw has been made.        
        """
        # Compares both lists to see whether either list contains a similar value. 
        if any(item in self.options for item in moves):

            # Returns a False value if the list contain similar values 
            return False
        else:
            # Returns a True value if the list do not contain similar values. 
            # Prints message notifying of the draw 
            print ("The game was a draw")
            return True

    def replay(self):
        """ 
        Check for replay of the game.

        This function checks to see whether a player would like to restart a new game. 
        
        Args:
        None.

        Returns:
        I f the player 


        Raises:
        
        """
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
    """ 
    ******* short Description*********

    ******* Long Description*********

    Args:

    Returns:

    Raises:
    
    """
    def __init__(self, opponent):
        self.moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.opponent = opponent
        self.opponent_symbol = []
        self.turn = []

    def out_going_message(self, symbol):
        """ 
        ******* short Description*********

        ******* Long Description*********

        Args:

        Returns:

        Raises:
        
        """
        moves = self.moves
        return (symbol, moves)


class Game ():
    """ 
    ******* short Description*********

    ******* Long Description*********

    Args:

    Returns:

    Raises:
    
    """

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
    """ 
    ******* short Description*********

    ******* Long Description*********

    Args:

    Returns:

    Raises:
    
    """
    print("""
 _______________  _________  _____  __________  ____
/_  __/  _/ ___/ /_  __/ _ |/ ___/ /_  __/ __ \/ __/
 / / _/ // /__    / / / __ / /__    / / / /_/ / _/  
/_/ /___/\___/   /_/ /_/ |_\___/   /_/  \____/___/  
""")
