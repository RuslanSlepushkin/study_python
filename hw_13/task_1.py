class Person:
    def __init__(self, firstname: str, lastname: str, age: int) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


    def talk(self) -> str:
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old.")


first_person = Person(firstname='Ruslan', lastname='Slepuhskin', age=29)
first_person.talk()