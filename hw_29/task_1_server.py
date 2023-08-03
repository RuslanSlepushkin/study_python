import socket

HOST = '127.0.0.1'
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print('UDP server is running. Waiting for messages:')

    while True:
        data, addr = s.recvfrom(1024)
        message = f"Message received: {data.decode('utf-8')}. If you want to get out, write 'quit'"
        s.sendto(message.encode('utf-8'), addr)
        print(f"Message '{data.decode('utf-8')}' from {addr}")

        if data.decode('utf-8') == 'quit':
            break