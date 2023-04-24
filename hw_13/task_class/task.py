# Задача 1: напишіть клас, котрий репрезентує фільм.
#
# Перенесіть код, котрий створює фільм в об'єктно-орієнтовану парадигму. Для цього створіть клас Film, котрий:
#
# 1. Приймає атрибути фільм
# 2. Валідує їх
# 3. Перевіряє їх на наявність необхідних полів
#
# Важливо: не чіпайте поки іншу функціональність застосунку.

from typing import Dict
from valid import ValidateName, ValidateYear, ValidateDirector, ValidateRank

name_input = input("Write the name of the film: ")
year_input = input("Write the year of the film: ")
imdb_input = input("Write the rating imdb of the film: ")
director_input = input("Write the name of the director of the film: ")


class Film:
    def __init__(self, **attributes: Dict) -> None:
        self.dict_validator = {
            'name': ValidateName(),
            'year': ValidateYear(),
            'director': ValidateDirector(),
            'imdb': ValidateRank(),
        }
        for attribute, value in attributes.items():
            if attribute in self.dict_validator.keys():
                    validator = self.dict_validator[attribute]
                    if validator.validate(value):
                        setattr(self, attribute, value)
                    else:
                        raise ValueError("Input data error")
            else:
                print("Not available field validator")


    def choice_film(self):
        greeting_film = print(f"The title of the movie {self.name} was released " +
                              f"in {self.year} directed by {self.director} and has an imdb rating of {self.imdb}.")
        return greeting_film


film = Film(name=name_input, year=year_input, imdb=imdb_input, director=director_input)
film.choice_film()