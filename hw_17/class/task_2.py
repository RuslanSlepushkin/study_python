# Задача 2:
#
# Напишіть ітератор, який буде повертати кожен N-й елемент заданого списку. Параметр N повинен задаватися при створенні ітератора.

from typing import Iterable, Iterator, Any


class MyIterable:
    def __init__(self, iterated_object: Iterable, n_element: int) -> None:
        self.iterated_object = iterated_object
        self.__index = 0
        self.n_element = n_element


    def __iter__(self) -> Iterator:
        return self


    def __next__(self) -> Any:
        if self.__index >= len(self.iterated_object):
            raise StopIteration("Iterations of all elements are performed")
        result = self.iterated_object[self.__index]
        self.__index += self.n_element
        return result


iterable = MyIterable([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)

result = ', '.join(str(item) for item in iterable)

print(result)