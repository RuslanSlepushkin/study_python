import socket

HOST = '127.0.0.1'
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        message = input()
        s.sendto(message.encode('utf-8'), (HOST, PORT))
        data, addr = s.recvfrom(1024)
        print(data.decode('utf-8'))

        if message == 'quit':
            break