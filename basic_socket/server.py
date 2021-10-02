try:
    from classes import *
except ModuleNotFoundError as import_error:
    print (import_error)
    exit()


def connect(self):
    """
    Starts server connection.

    Allows the server to starts listen for a client connection. Once the
    connection is made, it will wait to receive a message form the client.
    Once message has been recieved it will reply by sending the server
    username.

    Args:
    Takes in an instance of the Comms class and utilizes it's socket
    variables.

    Returns:
    Once the connection is made it will take in the opponents name and
    save it to the opponent variable within its Comms class

    Raises:
    ModuleNotFoundError if its unable to connect to the classes.py file.

    """
    # Starts Socket connection.
    self.socket.bind(self.addr)

    # listens for the client to connect.
    self.socket.listen(2)

    # Accepts the connection made.
    self.conn, self.addr = self.socket.accept()

    # Waits to receive the username from the client and save it as the
    # opponent variable
    self.opponent = self.receive()

    # Send the Severs user name to the client
    self.send(self.username)
    print ("Waiting for client to join....")

# Calls the Asci_art Class to display TIC TAC TOE artwork to user.
Asci_art()

# Save an instance of the Comms class giving the host computers
# IP address and players symbol. The IP address and automatically found.
server = Comms(socket.gethostbyname(socket.gethostname()), "x")

# Prints the servers IP address on the termina.
print(f"The server ip address:\n{server.server_ip}")

# Calls the connect function to start the connect with the client.
connect(server)

# Creates an instance of the User_info class and saves it to the game_info
# variable.
server.game_info = User_info(server.opponent)

# Sets the players turn to False.
server.game_info.turn = False

# Starts in instance of the Game class with the server instance as
# the argument.
Game().play(server)
