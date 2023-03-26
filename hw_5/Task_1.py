import random


list_number = list()
count = 0

while count < 10:
    number = random.randint(1, 100)
    list_number.append(number)
    count += 1

max_number = max(list_number)
print(list_number)
print(max_number)