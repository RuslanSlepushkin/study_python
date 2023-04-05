def count_lines(name):
    with open(name, 'r') as file:
        return len(file.readlines())


def count_chars(name):
    with open(name, 'r') as file:
        return len(file.read())


def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"Amount of lines: {lines}")
    print(f"Amount of chars: {chars}")
