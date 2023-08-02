from typing import Iterable, Iterator, Any


class MyIterable:
    def __init__(self, iterated_object: Iterable) -> None:
        self.iterated_object = iterated_object
        self.__index = 0


    def __iter__(self) -> Iterator:
        return self


    def __next__(self) -> Any:
        if self.__index >= len(self.iterated_object):
            raise StopIteration("Iterations of all elements are performed")
        result = self.iterated_object[self.__index]
        self.__index += 1
        return result


    def __getitem__(self, item) -> Any:
        return self.iterated_object[item]


iterable = MyIterable([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

result = ', '.join(str(item) for item in iterable)

print(result)
print(iterable[::-1])