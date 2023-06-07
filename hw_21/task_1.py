from typing import Any


class Stack:
    def __init__(self) -> None:
        self._stack = list()


    def push(self, element: Any) -> None:
        self._stack.append(element)


    def pop(self) -> Any:
        return self._stack.pop()


    def empty(self) -> bool:
        return len(self._stack) == 0


    def top(self) -> Any:
        return self._stack[-1]


    def reverse_order(self) -> Any:
        if not self.empty():
            return self._stack.pop(-1)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(True)
stack.push('False')

print(stack.reverse_order())
print(stack.reverse_order())
print(stack.reverse_order())
print(stack.reverse_order())