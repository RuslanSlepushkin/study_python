import asyncio


class AsyncioServer:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    async def listen_client(self, reader, writer) -> None:
        while True:
            print("Client connected")
            try:
                data = await reader.read(1024)
                if data:
                    writer.write(data)
                    await writer.drain()
                else:
                    raise Exception("Client disconnected")
            except Exception:
                break

    async def handle_client(self, reader, writer) -> None:
        task = asyncio.create_task(self.listen_client(reader, writer))
        try:
            await task
        finally:
            task.cancel()
            await task

    async def listen(self) -> None:
        server = await asyncio.start_server(self.handle_client, self.host, self.port)

        print(f"Waiting for connections on {self.host}:{self.port}...")

        async with server:
            await server.serve_forever()


async def main() -> None:
    server = AsyncioServer("127.0.0.1", 5000)
    await server.listen()


if __name__ == "__main__":
    asyncio.run(main())
