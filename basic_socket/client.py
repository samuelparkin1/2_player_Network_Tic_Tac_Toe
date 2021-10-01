try:
    from classes import *
except ModuleNotFoundError as import_error:
    print (import_error)
    exit()


def connect(self):
    self.socket.connect(self.addr)
    self.conn = self.socket
    self.send(self.username)
    self.opponent = self.receive()


Asci_art()
client = Comms(input("Please enter servers IP address\n"), "o")
try:
    connect(client)
except ConnectionRefusedError:
    print ("Server not connected...")
    exit()
client.game_info = User(client.opponent)
client.game_info.turn = True
Game().play(client)
