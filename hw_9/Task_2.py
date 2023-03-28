def calculate():
    a = int(input("Write number a: "))
    b = int(input("Write number b: "))
    value = (a**2)/b
    return value


try:
    print(calculate())
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Ooops, not number")