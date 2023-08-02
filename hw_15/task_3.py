from dataclasses import dataclass
from math import lcm


@dataclass
class Fraction:
    nominator: float
    denominator: float


    @classmethod
    def __validate_other(cls, other):
        if not isinstance(other, cls):
            raise TypeError("You cannot perform an operation on this object")
        else:
            return True


    def __add__(self, other) -> object:
        if self.__validate_other(other):
            new_denominator = lcm(self.denominator, other.denominator)
            left_nominator = int(new_denominator*self.nominator/self.denominator)
            right_nominator = int(new_denominator*other.nominator/other.denominator)
            result = Fraction(nominator= left_nominator + right_nominator, denominator = new_denominator)
        return result


    def __sub__(self, other) -> object:
        if self.__validate_other(other):
            new_denominator = lcm(self.denominator, other.denominator)
            left_nominator = int(new_denominator*self.nominator/self.denominator)
            right_nominator = int(new_denominator*other.nominator/other.denominator)
            result = Fraction(nominator= left_nominator - right_nominator, denominator = new_denominator)
        return result


    def __mul__(self, other) -> object:
        if self.__validate_other(other):
            new_nominator = self.nominator * other.nominator
            new_denominator = self.denominator * other.denominator
            result = Fraction(new_nominator, new_denominator)
        return result


    def __truediv__(self, other) -> object:
        if self.__validate_other(other):
            new_nominator = self.nominator * other.denominator
            new_denominator = self.denominator * other.nominator
            result = Fraction(new_nominator, new_denominator)
        return result


    def __eq__(self, other) -> bool:
        if self.__validate_other(other):
            result = self.nominator * other.denominator == other.nominator * self.denominator
        return result


    def __le__(self, other) -> bool:
        if self.__validate_other(other):
            result = self.nominator * other.denominator <= other.nominator * self.denominator
        return result


    def __lt__(self, other) -> bool:
        if self.__validate_other(other):
            result = self.nominator * other.denominator < other.nominator * self.denominator
        return result


    def __str__(self) -> str:
        return f"{self.nominator}/{self.denominator}"


x = Fraction(1, 2)
y = Fraction(1, 4)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x == y)
print(x != y)
print(x < y)
print(x <= y)
print(x > y)
print(x >= y)


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    assert x + y == Fraction(3, 4)
    assert x - y == Fraction(1, 4)
    assert x * y == Fraction(1, 8)
    assert x / y == Fraction(4, 2)
    assert (x == y) == False
    assert (x != y) == True
    assert (x < y) == False
    assert (x <= y) == False
    assert (x > y) == True
    assert (x >= y) == True