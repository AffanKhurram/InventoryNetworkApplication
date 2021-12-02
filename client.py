import socket
import pickle

HOST = '192.168.1.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    request = 'Request\nSorted Name'
    s.sendall(request.encode())
    data = s.recv(1024)

print('Received', pickle.loads(data))