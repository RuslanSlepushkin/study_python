from typing import Optional


def in_range(start, end: Optional[int] = None, step: int = 1) -> int:
    if end is None:
        end = start
        start = 0

    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step


ranges = [in_range(10), in_range(1, 10), in_range(1, 10, 2), in_range(10, 1, -1)]

for i in ranges:
    print(list(i))