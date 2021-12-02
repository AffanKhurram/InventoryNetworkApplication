import socket
import pickle

HOST = '192.168.1.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    request = 'Request\nSorted Name'
    s.sendall(request.encode())
    data = s.recv(1024)

s = data.decode()
lines = s.split('\n')
if lines[0].strip() == 'Response':
    # the inventory file was returned
    if lines[1].strip() == 'data':
        file_text = lines[2]
        # replace all ';' with \n as that is how the file was sent to us
        new_str = file_text.replace(';', '\n')
        # write this string to a file to get our new inventory
        with open('receiver/inventory.txt', 'w') as f:
            f.write(new_str)
    # Success message
    elif lines[1].strip() == 'success':
        pass
    # Some sort of error received
    elif lines[2].strip() == 'error':
        pass
    else:
        # Unknown response
        pass