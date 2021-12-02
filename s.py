import socket
from helper import delete, sorted, create_string, updated
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
                        print('Sorting by quantity')
                        file_text = create_string(sorted(1))
                        response = 'Response\ndata\n' + file_text
                        conn.sendall(response.encode())
                    elif line2[1] == 'Date':
                        print('Sorting by date')
                        file_text = create_string(sorted(2))
                        response = 'Response\nsuccess\n' + file_text
                        conn.sendall(response.encode())
                    else:
                        response = 'Response\nerror\nInvalid data field: ' + line2[1]
                        conn.sendall(response.encode())

                elif message_type == 'Update':
                    print("Entered update")
                    name = line2[1]
                    newq = line2[2]
                    print(name + " " + newq)
                    msg = updated(name, newq)
                    conn.sendall(msg.encode())

                elif message_type == "Delete":
                    print("Entered delete")
                    name = line2[1]
                    print(name)
                    msg = delete(name)
                    conn.sendall(msg.encode())

            else:
                conn.sendall(('Error, uknown message: ' + lines[0]).encode())
            


