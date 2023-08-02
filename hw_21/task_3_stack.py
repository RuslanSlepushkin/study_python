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


    def get_from_stack(self, element: Any) -> Any:
        if element not in self._stack:
            raise ValueError(f"{element} not in the stack")
        else:
            index = self._stack.index(element)
            return self._stack.pop(index)


stack = Stack()
stack.push(True)
stack.push(125)
stack.push('False')
stack.push(145)

print(stack.get_from_stack('False'))
print(stack._stack)