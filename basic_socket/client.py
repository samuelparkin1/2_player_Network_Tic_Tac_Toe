import socket, pickle
class ProcessData:
    def __init__(self, data= 'ABCDEFGHIJK'):
        self.data = data
    def __str__(self): return self.data

HOST = socket.gethostbyname(socket.gethostname()) #automatically gets ip address of computer
PORT = 50001
# Create a socket connection.
while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # Create an instance of ProcessData() to send to server.
    variable = input()
    # Pickle the object and send it to the server
    data_string = pickle.dumps(variable)

    s.send(data_string)

    #s.close()
    print ('Data Sent to Server')
    data = s.recv(40096)
    data_variable = pickle.loads(data)
    #conn.close()
    print (data_variable)
    print ('Data received from Server')
