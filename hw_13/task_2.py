class Dog:
    age_factor = 7


    def __init__(self, age: float) -> None:
        self.age = age


    def human_age(self):
        dog_age = self.age * self.age_factor
        return dog_age


dog = Dog(age=10)

print(dog.human_age())