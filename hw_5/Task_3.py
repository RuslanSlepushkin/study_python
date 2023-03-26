list_number = [i for i in range(1, 101)]
list_iter = list()
count = 0

while count <= len(list_number) - 1:
    if list_number[count] % 7 == 0 and list_number[count] % 5 != 0:
        list_iter.append(list_number[count])
    count += 1

print(list_iter)