import random

first_list = list()
second_list = list()
count = 0

while count < 10:
    first_list_number = random.randint(1, 10)
    second_list_number = random.randint(1, 10)
    first_list.append(first_list_number)
    second_list.append(second_list_number)
    count += 1

set_first_list = set(first_list)
set_second_list = set(second_list)
set_inter = set_first_list.intersection(set_second_list)
inter_list = list(set_inter)

print(first_list)
print(second_list)
print(inter_list)