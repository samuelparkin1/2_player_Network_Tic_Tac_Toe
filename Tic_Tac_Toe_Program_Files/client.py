try:
    from classes import *
except ModuleNotFoundError as import_error:
    print (import_error)
    exit()


def connect(self):
    """
    Starts client connection.

    Allows the client to connect to the server. Once the connection is made,
    it will send the clients user name to the server as a message.
    Once message has been sent, it will wait for a reply from the server with
    its user name.

    Args:
    Takes in an instance of the Comms class and utilizes it's socket
    variables.

    Returns:
    Once the connection is made it will take in the opponents name and
    save it to the opponent variable within its Comms class

    Raises:
    ModuleNotFoundError if its unable to connect to the classes.py file.

    """
    # Looks for the connection with the server.
    self.socket.connect(self.addr)

    # Save a copy of the socket connection. This is used for sending and
    # receiving messages.
    self.conn = self.socket

    # Send the clients user name to the server.
    self.send(self.username)

    # Waits to receive the username from the server and save it as the
    # opponent variable.
    self.opponent = self.receive()

# Calls the Asci_art Class to display TIC TAC TOE artwork to user.
Asci_art()

# Save an instance of the Comms class giving the host computers
# IP address and players symbol.
client = Comms(input("Please enter servers IP address\n"), "o")


try:
    # Calls the connect function to start the connect with the client.
    connect(client)
except ConnectionRefusedError:
    # If Unable to connect to the server, prints a message to the terminal.
    print ("Server not connected...")
    # Exit the programme
    exit()
except socket.gaierror:
    print ("Incorrect IP address has been entered")
    # Exit the programme
    exit()

# Creates an instance of the User_info class and saves it to the game_info
# variable.
client.game_info = User_info(client.opponent)

# Sets the players turn to True.
client.game_info.turn = True

# Starts in instance of the Game class with the clients instance as
# the argument.
Game().play(client)
