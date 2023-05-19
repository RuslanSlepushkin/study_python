from functools import wraps
from typing import Callable


class TypeDecorators:
    @staticmethod
    def to_int(func) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> int:
            result = func(*args, **kwargs)
            try:
                return int(result)
            except Exception:
                print("It is not possible to convert function results to a given type")
                return result
        return wrapper


    @staticmethod
    def to_str(func) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            result = func(*args, **kwargs)
            try:
                return str(result)
            except Exception:
                print("It is not possible to convert function results to a given type")
                return result
        return wrapper


    @staticmethod
    def to_bool(func) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> bool:
            result = func(*args, **kwargs)
            try:
                return bool(result)
            except Exception:
                print("It is not possible to convert function results to a given type")
                return result
        return wrapper


    @staticmethod
    def to_float(func) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> float:
            result = func(*args, **kwargs)
            try:
                return float(result)
            except Exception:
                print("It is not possible to convert function results to a given type")
                return result
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25

assert do_something('True') is True