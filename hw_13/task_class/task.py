# Задача 1: напишіть клас, котрий репрезентує фільм.
#
# Перенесіть код, котрий створює фільм в об'єктно-орієнтовану парадигму. Для цього створіть клас Film, котрий:
#
# 1. Приймає атрибути фільм
# 2. Валідує їх
# 3. Перевіряє їх на наявність необхідних полів
#
# Важливо: не чіпайте поки іншу функціональність застосунку.

from valid import validate_name, validate_year, validate_director, validate_rank

name_input = input("Write the name of the film: ")
year_input = input("Write the year of the film: ")
imdb_input = input("Write the rating imdb of the film: ")
director_input = input("Write the name of the director of the film: ")


class Film:
    def __init__(self, name: str, year: str, imdb: str, director: str):
        is_name_valid = validate_name(name)
        if is_name_valid:
            self.name = name
        else:
            raise ValueError

        is_year_valid = validate_year(year)
        if is_year_valid:
            self.year = year
        else:
            raise ValueError

        is_rank_valid = validate_rank(imdb)
        if is_rank_valid:
            self.imdb = imdb
        else:
            raise ValueError

        is_director_valid = validate_director(director)
        if is_director_valid:
            self.director = director
        else:
            raise ValueError


    def choise_film(self):
        greeting_film = print(f"The title of the movie {self.name} was released " +
                              f"in {self.year} directed by {self.director} and has an imdb rating of {self.imdb}.")
        return greeting_film


film = Film(name=name_input, year=year_input, imdb=imdb_input, director=director_input)
film.choise_film()
