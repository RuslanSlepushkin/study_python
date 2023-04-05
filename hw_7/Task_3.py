def do_add(values):
    answer = 0
    for value in values:
        answer += value
    return answer


def do_difference(values):
    first_number = values[0]
    for value in values[1:]:
        first_number -= value
    return first_number


def do_multiply(values):
    answer = 1
    for value in values:
        answer *= value
    return answer


def make_operation(operator, *numbers):
    dict_operation = {
        '+': do_add(numbers),
        '-': do_difference(list(numbers)),
        '*': do_multiply(numbers)
    }
    return dict_operation[operator]


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6,))