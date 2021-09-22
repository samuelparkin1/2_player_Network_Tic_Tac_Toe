class ProcessData:
    def __init__(self, data= 'ABCDEFGHIJK'):
        self.data = data
    def __str__(self): return self.data

import socket, pickle




print ("Server is Listening.....")
HOST = socket.gethostbyname(socket.gethostname()) #automatically gets ip address of computer
PORT = 50001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while True:
    s.listen(1)
    conn, addr = s.accept()
    print ('Connected by', addr)
    data = conn.recv(4096)
    data_variable = pickle.loads(data)
    #conn.close()
    print (data_variable)
    print ('Data received from client')

    variable = input()
    # Pickle the object and send it to the server
    data_string = pickle.dumps(variable)
    conn.send(data_string)
    #s.close()
    print ('Data Sent to client')
