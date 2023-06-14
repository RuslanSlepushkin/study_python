import socket
import task_2_caesar

HOST = '127.0.0.1'
PORT = 5000

data = input("Enter the data to be transferred: ")
key = input("Enter the encryption key: ")
message = f"{data}:{key}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))


    s.sendall(message.encode('utf-8'))

    data_server = s.recv(1024).decode('utf-8')
    data_decode = task_2_caesar.decode(data_server, int(key))

    print(data_decode)