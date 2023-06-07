open_brackets = ["[", "{", "("]
close_brackets = ["]", "}", ")"]


def check(sequence: str) -> bool:
    stack = []

    for i in sequence:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            index = close_brackets.index(i)
            if len(stack) > 0 and open_brackets[index] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


sequences = ['{[]{()}}', '(()', '({}{}][)', '{{]({}}[}']

for sequence in sequences:
    if check(sequence):
        print("Sequence is balanced")
    else:
        print("Sequence isn't balanced")