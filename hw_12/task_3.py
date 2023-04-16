def arg_rules(type: type, max_length: int, contains: list):
    def decorate(func: callable):
        def wrapper(name: str) -> str:
            if not isinstance(name, type):
                print("Incorrect type of argument.")
                return False
            elif len(name) > max_length:
                print("Incorrect maximum length argument.")
                return False
            elif len(name) < max_length:
                for item in contains:
                    if item not in name:
                        print("The maximum length of the argument is exceeded.")
                        return False
            return func(name)
        return wrapper
    return decorate


@arg_rules(type=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

assert create_slogan('Ruslan') is False

assert create_slogan(14) is False