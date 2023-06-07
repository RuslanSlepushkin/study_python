from typing import Any


class Queue:
    def __init__(self) -> None:
        self._queue = list()


    def put(self, element) -> None:
        self._queue.append(element)


    def get(self) -> Any:
        return self._queue.pop(0)


    def is_empty(self) -> bool:
        return len(self._queue) == 0


    def get_from_queue(self, element: Any) -> Any:
        if element not in self._queue:
            raise ValueError(f"{element} not in the queue")
        else:
            index = self._queue.index(element)
            return self._queue.pop(index)


queue = Queue()
queue.put(True)
queue.put('False')
queue.put(1)
queue.put(5)

print(queue.get_from_queue('False'))
print(queue._queue)