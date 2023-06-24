import asyncio


class AsyncioServer:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    async def handle_client(self, reader, writer) -> None:
        while True:
            data = await reader.read(1024)

            if not data:
                break

            message = data.decode().strip()
            print(f"Received message: {message}")
            writer.write(data)
            await writer.drain()

        print("Client disconnected")
        writer.close()

    async def listen(self) -> None:
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        address = server.sockets[0].getsockname()
        print(f"Server started on {address}")

        async with server:
            await server.serve_forever()


asyncio.run(AsyncioServer("127.0.0.1", 5000).listen())
