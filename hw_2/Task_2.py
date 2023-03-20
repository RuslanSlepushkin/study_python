name = 'Ruslan'
surname = ' Slepushkin'

# первый вариант
full_name = name + surname
print("Greetings", full_name + '.')
# второй вариант
full_name_second = ''.join((name, surname))
print("Greetings", full_name_second + '.')
# третий вариант
full_name_third = '{}{}'.format(name, surname)
print("Greetings", full_name_third + '.')