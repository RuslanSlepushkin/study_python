# Задача 2. Система планет.
#
# Створити клас "Планета" з наступними атрибутами: ім'я, радіус та маса.
# Створити клас "Планетна система", що містить список планет. Додати метод "додати планету", що додає планету до списку.
# Створити об'єкт "планетна система", додати до нього кілька планет та викликати метод "додати планету".

import json
from collections import namedtuple


class ThePlanetarySystem:
    def __init__(self, title: str) -> None:
        self.title = title
        self.planets_list_namedtuple = list ()


    def add_planet(self, planet: tuple) -> None:
        self.planets_list_namedtuple.append(planet)


    def put_json(self) -> None:
        planets_list_dict = [planet_namedtuple._asdict() for planet_namedtuple in self.planets_list_namedtuple]
        system_dict = {
            solar_system.title: planets_list_dict,
        }
        with open(f'{self.title}.json', 'w') as file_json:
            json.dump(system_dict, file_json)


solar_system = ThePlanetarySystem('Solar system')

Planet = namedtuple('Planet', ['title', 'radius', 'mass'])

mercury = Planet('Mercury', 2440.0, 3.30E20)
venus = Planet('Venus', 6052.0, 4.87E21)
earth = Planet('Earth', 6371.0, 5.97E21)
mars = Planet('Mars', 3390.0, 6.39E20)
jupiter = Planet('Jupiter', 69911.0, 1.90E24)
saturn = Planet('Saturn', 58232.0, 5.68E23)
uranus = Planet('Uranus', 25362.0, 8.68E22)
neptune = Planet('Neptune', 24622.0, 1.02E23)

solar_system.add_planet(mercury)
solar_system.add_planet(venus)
solar_system.add_planet(earth)
solar_system.add_planet(mars)
solar_system.add_planet(jupiter)
solar_system.add_planet(saturn)
solar_system.add_planet(uranus)
solar_system.add_planet(neptune)

solar_system.put_json()