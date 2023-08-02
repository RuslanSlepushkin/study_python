from abc import abstractmethod, ABC


class Animal(ABC):
    @abstractmethod
    def talk(self) -> None:
        pass


class Dog(Animal):
    def talk(self) -> None:
        print("woof woof")


class Cat(Animal):
    def talk(self) -> None:
        print("meow")


def animal_talk(animal: Animal) -> None:
    animal.talk()


animals = [Cat(), Dog()]

for animal in animals:
    animal_talk(animal)