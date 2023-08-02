from typing import Any, Optional


class Node:
   def __init__(self, data: Any) -> None:
      self.data = data
      self.next = None


class Queue:
   def __init__(self) -> None:
      self.head = None
      self.last = None

   def enqueue(self, data: Any) -> None:
      if self.last is None:
         self.head = Node(data)
         self.last = self.head
      else:
         self.last.next = Node(data)
         self.last = self.last.next

   def dequeue(self) -> Optional[Node]:
      if self.head is None:
         return None
      else:
         data = self.head.data
         self.head = self.head.next
         return data