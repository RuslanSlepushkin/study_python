import socket
from threading import Thread


class ThreadServer:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self) -> None:
        self.sock.listen(5)
        print("Wait connection....")

        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            Thread(target=self.listen_client, args=(client)).start()

    def listen_client(self, client: str) -> None:
        with client:
            while 1:
                print("Client connected")
                try:
                    data = client.recv(1024)
                    if data:
                        client.sendall(data)
                    else:
                        raise ("Client disconnected")
                except Exception:
                    break


ThreadServer("127.0.0.1", 5000).listen()
