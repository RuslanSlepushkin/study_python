# Задача 3: Перевірити чи є рядок паліндромом використовуючи deque
from collections import deque


def is_palindrom(word: str) -> bool:
    word_deque = deque(word)

    while len(word_deque) > 1:
        if word_deque.popleft() != word_deque.pop():
            return False

    return True


word = 'tenet'

if is_palindrom(word):
    print(f"It's a palindrom!")
else:
    print(f"It's not a palindrom!")