from typing import List


class Mathematician:
    def square_nums(self, numbers: List) -> List:
        result = list(map(lambda x: pow(x, 2), numbers))
        return result


    def remove_positives(self, numbers: List) -> List:
        result = list(filter(lambda x: x <= 0, numbers))
        return result


    def filter_leaps(self, numbers: List) -> List:
        result = list()
        for number in numbers:
            if number % 4 == 0 and (number % 100 != 0 or number % 400 == 0):
                result.append(number)
        return result


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]