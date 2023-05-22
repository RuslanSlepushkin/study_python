class FileManager:
    counter = 0


    def __init__(self, filename: str, mode='r') -> None:
        self.filename = filename
        self.mode = mode
        self.file = None


    @staticmethod
    def __write_log(cls, message: str):
        with open('logging.txt', 'a') as log_file:
            log_file.write(message + '\n')


    def __enter__(self):
        self.file = open(self.filename, self.mode)
        FileManager.counter += 1
        return self.file


    def __exit__(self, exc_type, exc_val, exc_tb):
        FileManager.counter -= 1
        self.file.close()

        if exc_type is not None:
            __write_log(f"Exception: {exc_type}, {exc_val}")


with FileManager('test.txt', 'w') as file:
    file.write("Hello World!")