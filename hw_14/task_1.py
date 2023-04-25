from dataclasses import dataclass
from abc import ABC


@dataclass
class Person(ABC):
    name: str
    surname: str
    age: int


    def greeting(self) -> None:
        print(f'Hello!')


@dataclass
class Teacher(Person):
    subject: str
    salary: float


    def greeting(self) -> None:
        super().greeting()
        len_subject = len(self.subject)
        print(f"My name is {self.name} and I'm your teacher {self.subject:!<{len_subject + 1}}")


@dataclass
class Student(Person):
    grade: str


    def greeting(self) -> None:
        super().greeting()
        print(f"My name is {self.name} and I'm from {self.grade} class!")


class Security(Person):
    pass


ruslan = Student('Ruslan', 'Slepushkin', 29, '11-A')
guido = Teacher('Guido', "van Rossum", 67, 'Python', 0.99)
security = Security('Harry', 'Hole', 57)

guido.greeting()
ruslan.greeting()
security.greeting()

print(security.name)