def with_index(iterable, start: int = 0) -> tuple:
    i = start
    for item in iterable:
        yield i, item
        i += 1


gen = with_index('Python', 1)

for i, item in gen:
    print(item, i)