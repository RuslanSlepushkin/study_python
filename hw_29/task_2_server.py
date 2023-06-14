import socket
import task_2_caesar

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f'Wait connection....')
    conn, addr = s.accept()

    while conn:
        print("Client connected")
        message = conn.recv(1024).decode('utf-8')
        data, key = message.split(':')

        data_encode = task_2_caesar.encode(data, int(key))
        conn.sendall(data_encode.encode('utf-8'))