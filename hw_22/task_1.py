from typing import Any, Optional


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class UnorderedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.head == None

    def add(self, data: Any) -> None:
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def append(self, data: Any) -> None:
        cur = self.head
        if cur is None:
            self.add(data)
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(data)

    def index(self, data: Any) -> int:
        cur = self.head
        index = 0

        while cur is not None:
            if cur.data == data:
                return index
            cur = cur.next
            index += 1

        raise ValueError(f"{data} is not in the list")

    def pop(self, index: Optional[int] = None) -> Any:
        if self.is_empty():
            raise IndexError(f"List is empty")
        if index is None:
            index = self.size - 1
        if index == 0:
            item = self.head.data
            self.head = self.head.next
            return item

        cur = self.head
        prev = None
        count = 0

        while cur is not None and count < index:
            prev = cur
            cur = cur.next
            count += 1

        if cur is None:
            raise IndexError(f"Index out of range")

        item = cur.data

        if cur.next is None:
            prev.next = None
        else:
            prev.next = cur.next

        return item

    def insert(self, index: int, data: Any) -> None:
        if index == 0:
            self.add(data)
        else:
            cur = self.head
            prev = None
            count = 0

            while cur is not None and count < index:
                prev = cur
                cur = cur.next
                count += 1

            if count < index:
                raise IndexError(f"Index out of range")

            temp = Node(data)
            prev.next = temp
            temp.next = cur

    def slice(self, start: int, stop: int) -> object:
        if start < 0 or start >= stop:
            raise ValueError(f"Invalid slice parameters")

        cur = self.head
        count = 0

        while cur is not None and count < start:
            cur = cur.next
            count += 1

        if cur is None:
            raise ValueError(f"Start position out of range")

        result = UnorderedList()

        while cur is not None and count < stop:
            result.append(cur.data)
            cur = cur.next
            count += 1

        return result