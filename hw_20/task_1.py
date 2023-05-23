from typing import List, Tuple

# We assume that all lists passed to functions are the same length N

# Match big O complexities with the code snippets below

# answers
# 1 - n - Використовується один цикл з однією нескінченною змінною О(first_list) = O(n)
# 2 - 1 - Використовується один цикл із фіксованою кількістю ітерацій О(10) = O(1)
# 3 - n^2 - Використовується два цикли в кожному з яких є по одній нескінченній змінній O(first_list * second_list) = O(n * m)
# 4 - n - Використовується один цикл з однією нескінченною змінною О(input_list) = O(n)
# 5 - n^2 - Використовується два цикли в кожному з яких є по одній нескінченній змінній O(n * n) = O(n^2)
# 6 - log n - Використовується один цикл з однією нескінченною змінною, яка за кожну ітерацію зменшується вдвічі О(n/2) = O(log n)


def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n


def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(second_list)
    return temp


def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res


def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res


def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n