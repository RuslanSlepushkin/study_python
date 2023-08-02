class CustomException(Exception):
    def __init__(self, message: str):
        self.message = message
        with open('logs.txt', 'a') as file:
            file.write(message + '\n')


custom_error = CustomException("You did something wrong!")

try:
    raise custom_error
except CustomException:
    print(f"Caught the error CustomException: {custom_error.message}")
