def oops():
    raise IndexError


def catch_error():
    try:
        oops()
    except IndexError:
        print("Caught error")


catch_error()
# Если вызвать KeyError вместо IndexError, тогда функция catch_error не сможет перехватить исключение и выведется ошибка.