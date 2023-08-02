# Задача 1. Геометричні фігури.
#
# Створіть базовий клас "Фігура", який містить методи для обчислення площі та периметру фігури.
# Створіть класи "Прямокутник", "Круг" та "Трикутник", які успадковуються від класу
# "Фігура" і мають свої власні методи для обчислення площі та периметру.

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass


    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if side_a+side_b < side_c or side_a+side_c < side_b or side_b+side_c < side_a:
            raise ValueError


    def perimeter(self) -> float:
        result = self.side_a + self.side_a + self.side_a
        return result


    def area(self) -> float:
        hp = self.perimeter()/2
        result = (hp*(hp - self.side_a)*(hp - self.side_b)*(hp - self.side_c)) ** 0.5
        return result


class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width


    def perimeter(self) -> float :
        result = (self.length + self.width) * 2
        return result


    def area(self) -> float:
        result = self.length * self.width
        return result


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius


    def perimeter(self) -> float:
        result = pi * self.radius * 2
        return result


    def area(self) -> float:
        result = pi * (pow(self.radius, 2))
        return result