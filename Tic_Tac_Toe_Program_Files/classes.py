import os
import socket
import pickle


class Comms():
    """Socket communication variables.

    This class contains the variable needed for a socket connection.
    This class can be utilized by either the server.py or the client.py.
    This class contains functions that preform the sending and receiving of messages over the socket connection.

    Args:
    Takes in the IP address of the server.
    Takes in the players symbol for the game.

    Returns:
    None

    """
    def __init__(self, server_ip, symbol):
        # The IP address of the server.
        self.server_ip = server_ip

        # The port number for the connection.
        self.port = 50053

        # Creates an instance of a socket connect over IPV4 TCP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Prevents changing port number if the port number is in use.
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Saves the the IP address and port number to a single variable.
        self.addr = (self.server_ip, self.port)

        # Asks the user to input their name.
        self.username = input("What's your players name? ").capitalize()

        # Save the symbol of the user. This is used during the play
        # of the game.
        self.symbol = symbol

        # Variable used to save the users information during the play
        # of the game.
        self.game_info = []

    def send(self, message):
        """Sends messages over the sockets connection.

        This function is called when the user needs to send a message
        over the socket connection.
        The message is transmitted as a pickle.

        Args:
        Takes in the variable or object that needs to be sent.

        Returns: None
        """

        # The variable or object is converted to a pickle.
        sending_msg = pickle.dumps(message)

        # Sends the message over the socket connection.
        self.conn.send(sending_msg)

    def receive(self):
        """Receives message over the sockets connection.

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

            # Converts the message from a pickle back to a variable or object.
            received_msg = pickle.loads(data)

            # Once message has been received it returns the message.
            if received_msg:
                return (received_msg)
            break


class Board():
    """Displays the board to the user.

    The Board class is used to take in the moves that have been made
    and display the TIC TAC TOE board with those moves.

    Args: Takes in the positions/moves of the game.

    Returns: None
    """

    def __init__(self, positions):
        self.positions = positions

    def grid(self,):
        """Prints the board.

        Prints the TIC TAC TOE board with either the moves that have been
        made or the available spotsthe user can select.

        Args: Takes in the postions that have been made by the users

        Returns: None.
        """

        print ('-------------')
        print ('| ' + self.positions[6] + ' | ' + self.positions[7] + ' | ' + self.positions[8] + ' | ')
        print ('-------------')
        print ('| ' + self.positions[3] + ' | ' + self.positions[4] + ' | ' + self.positions[5] + ' | ')
        print ('-------------')
        print ('| ' + self.positions[0] + ' | ' + self.positions[1] + ' | ' + self.positions[2] + ' | ')
        print ('-------------\n')


class Tic_Tac_Toe():
    """TIC TAC TOE game functions.

    This class contains the functions needed to play the game TIC TAC TOE.
    Each functions will call their own arguments that are needed for it to execute
    correctly.

    Args:
    None.

    Returns:
    None.
    """

    def __init__(self):

        # These options are referenced as allowable moves that the player
        # can select during the game.
        self.options = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

    def user_select(self, moves, symbol):
        """Player to select their move.

        This function is called when the player needs to select the move
        they wish to make.

        Args:
        Takes in the moves that have been made and available spots on the
        board. It then checks to wether the the selected move is available.

        Returns:
        Update the moves that have been made and returns it to the user.

        """
        # Take in the list of moves that have been made.
        self.moves = moves

        # Takes in the players symbol that is making a move.
        self.symbol = symbol

        while True:
            # Asks the user to input their move.
            user_input = input(f"Using the corresponding numbers,\nselect a position for your marker? ('{self.symbol}') ")

            # Check to see if the user has selected a move that is between
            # 1-9 of the grid.
            if user_input in self.options:

                # Checks to see if the user has selected a number that has already been
                # taken.
                if str(user_input) in self.moves:

                    # Updates the list of moves made with the position the
                    # user selected. Replaces the number in the list with
                    # the players symbol.
                    self.moves[int(user_input)-1] = str(self.symbol)
                    break
                else:
                    # Notifies user the they have selected a number that
                    # has already been taken
                    print ("\nSorry, that position has been taken.\n")
            else:
                # notifies user they have not put in a valid move.
                print ("Sorry but that is an invalid input.")

    def win_check(self, moves, symbol, player):
        """Checks if the move has won the game.

        This will check to see if the move that's been made has won the
        game.

        Args:
        Takes in the list of moves, the players symbol and the players name.

        Returns:
        If the player has won the game it will return a True value and
        a message notifying the user of the win.
        If no win was made it wil return a False value.
        """
        # Will go though every possible winning move to check if they
        # contain the players symbol.
        if (
            (moves[0] == moves[1] == moves[2] == symbol) or
            (moves[3] == moves[4] == moves[5] == symbol) or
            (moves[6] == moves[7] == moves[8] == symbol) or
            (moves[0] == moves[3] == moves[6] == symbol) or
            (moves[1] == moves[4] == moves[7] == symbol) or
            (moves[2] == moves[5] == moves[8] == symbol) or
            (moves[0] == moves[4] == moves[8] == symbol) or
            (moves[2] == moves[4] == moves[6] == symbol)
        ):
            # Prints message to user of the win of the game.
            print (f"{player} won the game")

            # Returns a true value.
            return True
        else:
            # Returns a False value.
            return False

    def draw(self, moves,):
        """Checks for a draw in the game.

        This will check if there are any available spots left on the board,
        If not it will call a draw of the game.

        Args:
        Takes in the moves made by the players and move options.

        Returns:
        Returns a False value is no draw was made.
        Returns a True value if a draw has been made.
        """
        # Compares the players move list and the move option list to see
        # whether either list contains a similar value.
        if any(item in self.options for item in moves):

            # Returns a False value if the list contain similar values
            return False
        else:
            # Returns a True value if the lists do not contain similar
            # values.
            # Prints message notifying of the draw
            print ("The game was a draw")
            return True

    def replay(self):
        """Check for a replay of the game.

        This function checks to see whether a player would like to restart
        a new game.

        Args:
        None.

        Returns:
        If the player wishes to play again it will return a True value.
        if the play does no want to play again it will return a False value.
        """

        while True:
            # Asks for the user to input whether they want to play again.
            play_again = input("Would you like to play agin? ").capitalize
            print (play_again())

            # If the input starts with a Y, return True.
            if play_again()[0] == "Y":
                return True

            # If the input starts with a N, return False.
            if play_again()[0] == "N":
                return False

            # If the user has inputted a valuse other than yes or no, it will
            # ask for the correct input.
            else:
                print("Please enter Yes/No ")


class User_info():
    """Information about the player for a siglar round of game,

    This creates class object that contains information about the user
    during a game. It saves a list of moves that have been made, the
    opponents name, the opponents symbol, and whether it's the players turn.
    With this information it will also creates a list of variabal to send
    to the opponent.

    Args:
    Takes in the opponents name and symbol.

    Returns:
    A list of variables to send to the opponent.
    """
    def __init__(self, opponent):
        self.moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.opponent = opponent
        self.opponent_symbol = []
        self.turn = []

    def out_going_message(self, symbol):
        """
        Send players variables to opponent.

        This will make a list of the players moves and symbol variable to
        send to the opponent.

        Args:
        Takes the players symbol and list of moves.

        Returns:
        A list containing the players moves and symbol.
        """
        moves = self.moves
        return (symbol, moves)


class Game ():
    """
    Contains the function to start playing of the game.

    Args:
    None.


    Returns: None
    """

    connected = True

    def play(self, player):
        """
        Start playing the game.

        This Class is used to controls the flow of the TIC TAC TOE game.
        It will run though the sequence of the game, calling the appropriate
        Classes to run when needed.

        Args:
        It takes in the instance of either the sever or client, utilizing their
        variables such us the socket connection settings for sending and
        receiveing messages, the players name and the players symbol.
        Also the User class they inherited which contains,
        their moves, their opponents name, and opponents symbol.

        Returns: None

        Raises:
        EOFError - This will occur if the connection with the opponent has
        been lost.
        """

        self.player = player
        # The game will continue to run until the player stops the connection.
        while self.connected:

            # Will attempt to run the game function
            try:
                # will continue with the current game while game_play is true.
                self.game_play = True
                while self.game_play:

                    # Clears the players terminal screen.
                    os.system('cls||clear')
                    Asci_art()

                    # Calls the Board class to print the board
                    Board(player.game_info.moves).grid()

                    # Check if the players turn is True.
                    if player.game_info.turn:

                        # Calls the user_select function so the player can input their move.
                        Tic_Tac_Toe().user_select(player.game_info.moves, player.symbol)

                        # Sends the players move to the opponent.
                        player.send(player.game_info.out_going_message(player.symbol))

                        # Turns the players turn to False.
                        player.game_info.turn = False

                        # Clears the players terminal screen.
                        os.system('cls||clear')
                        Asci_art()

                        # Calls the Board class to print the board
                        Board(player.game_info.moves).grid()

                        # Calls the win_check and draw functions to check players move.
                        # If either return True it will continue.
                        if (Tic_Tac_Toe().win_check(player.game_info.moves,
                            player.symbol, "You have") or
                                Tic_Tac_Toe().draw(player.game_info.moves)):

                            # Calls the replay function to see if the player wants to
                            # play again.
                            if Tic_Tac_Toe().replay():

                                # Resets the User_info class for a new game.
                                player.game_info = User_info(player.game_info.opponent)

                                # Sets game_play to false to restart the game.
                                self.game_play = False
                            else:
                                # Closes the socket connection.
                                player.socket.close()

                                # Sets connection to false to end the game function.
                                self.connected = False
                                break

                    else:
                        # Prints a message to the player "Waiting for the opponent to make
                        # a move."
                        print (f"Waiting for {player.game_info.opponent} to make a move.")

                        # Starts the players receive function to receive a message for
                        # the opponents containing their moves and symbol.
                        player.game_info.opponent_symbol, player.game_info.moves = player.receive()

                        # Clears the players terminal screen.
                        os.system('cls||clear')
                        Asci_art()

                        # Calls the Board class to print the TIC TAC TOE board.
                        Board(player.game_info.moves).grid()

                        # Calls the win_check and draw functions to check the opponents
                        # move. If either return True it will continue.
                        if (Tic_Tac_Toe().win_check(
                                player.game_info.moves,
                                player.game_info.opponent_symbol,
                                f"{player.opponent} has") or
                                Tic_Tac_Toe().draw(player.game_info.moves)):

                            if Tic_Tac_Toe().replay():

                                # Resets the User_info class for a new game.
                                player.game_info = User_info(player.game_info.opponent)

                                # Sets game_play to False to restart the game.
                                self.game_play = False
                            else:
                                # Closes the socket connection.
                                player.socket.close()

                                # Sets connection to False to end the game function.
                                self.connected = False
                                break

                        # Turns the players turn to True.
                        player.game_info.turn = True

            except EOFError:
                # Closes the socket connection
                player.socket.close()

                # Print a message to the player notifying them the the opponent has left
                # the game.
                print (input(f"Looks like {player.opponent} has disconnected. Press Enter to end game"))

                # Sets connection to False to end the game function.
                self.connected = False


class Asci_art():

    def __init__(self):
        """Game title Asci art

        This will dispay the game title as Asci art to the user.

        """
        print("""
 _______________  _________  _____  __________  ____
/_  __/  _/ ___/ /_  __/ _ |/ ___/ /_  __/ __ \/ __/
 / / _/ // /__    / / / __ / /__    / / / /_/ / _/
/_/ /___/\___/   /_/ /_/ |_\___/   /_/  \____/___/
""")
