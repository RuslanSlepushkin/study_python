from typing import Any, Optional


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None


    def is_empty(self) -> bool:
        return True if self.head == None else False


    def push(self, data) -> None:
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node


    def top(self) -> Optional[Node]:
        if self.is_empty():
            return None
        else:
            return self.head.data


    def pop(self) -> Optional[Node]:
        if self.is_empty():
            return None
        else:
            pop_node = self.head
            self.head = self.head.next
            pop_node.next = None
            return pop_node.data