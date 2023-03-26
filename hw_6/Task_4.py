list_weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dict_weekday = {i+1: day for i, day in enumerate(list_weekday)}
dict_weekday_reverse = {day: i+1 for i, day in enumerate(list_weekday)}
print(list_weekday)
print(dict_weekday)
print(dict_weekday_reverse)
