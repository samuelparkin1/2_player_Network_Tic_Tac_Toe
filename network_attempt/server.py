import socket 
import threading
import pickle

class Server():

    def __init__(self):
        self.header = 64
        self.port = 5055
        self.server_ip = socket.gethostbyname(socket.gethostname())
        self.address = (self.server_ip, self.port)
        self.format = 'utf-8'
        self.disconnect_message = "!DISCONNECT"
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(self.address)
        self.client_list = {}

    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")


        connected = True
        while connected:
            msg_length = conn.recv(10000)
            if msg_length:
                msg = pickle.loads(msg_length)
                if msg == self.disconnect_message:
                    connected = False
                print (msg)

        conn.close()
        '''
        connected = True
        while connected:
            msg_length = conn.recv(self.header).decode(self.format)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.format)
                if msg == self.disconnect_message:
                    connected = False

                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode(self.format))

        conn.close()
        '''       

    def start(self):
        self.server_socket.listen(2)
        print(f"[LISTENING] Server is listening on {self.server_ip}")
        while True:
            conn, addr = self.server_socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] self.server_socket is starting...")
server1 = Server()

server1.start()