import socket
from helper import sorted, create_string
import pickle

HOST = '192.168.1.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn: 
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            # Parse the request
            lines = data.split('\n')
            if lines[0].strip() == 'Request':
                # handle request
                line2 = lines[1].split()
                message_type = line2[0]
                if message_type == 'Sorted':
                    if line2[1] == 'Name':
                        print('Sorting by name')
                        file_text = create_string(sorted(0))
                        response = 'Response\ndata\n' + file_text
                        conn.sendall(response.encode())
                    elif line2[1] == 'Quantity':
                        sorted(1)
                    elif line2[1] == 'Date':
                        sorted(2)
                    else:
                        conn.sendall(('Invalid data field: ' + line2[1]).encode())

            else:
                conn.sendall(('Error, uknown message: ' + lines[0]).encode())
            


