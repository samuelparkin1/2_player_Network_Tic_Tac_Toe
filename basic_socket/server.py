try:
    import socket
    from classes import *
except ModuleNotFoundError as import_error:
    print (import_error)
    exit()


def connect(self):
    self.socket.bind(self.addr)
    self.socket.listen(2)
    self.conn, self.addr = self.socket.accept()
    self.opponent = self.receive()
    self.send(self.username)

Asci_art()
server = Comms(socket.gethostbyname(socket.gethostname()), "x")
print(f"The server ip address:\n{server.server_ip}")
connect(server)
print ("Waiting for client to join....")
server.game_info = User(server.opponent)
server.game_info.turn = False
Game().play(server)
