from functools import wraps


def logger(func: callable):
    @wraps(func)
    def wrapper(*args):
        print(f"Name function is '{func.__name__}' and arguments are {args}.")
    return wrapper


@logger
def add(x: int, y: int) -> int:
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


square_all(4, 5, 10, 12)
add(4, 5)