import random


in_string = input("Write word: ")
count = 0
while count < 5:
    list_num_string = random.sample(in_string, len(in_string))
    num_string_refresh = ''.join(list_num_string)
    print(num_string_refresh)
    count += 1