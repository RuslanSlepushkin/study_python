# Задача 2. Робота з файлами через map.
#
# В директорії titanic_data ви можете знайти файл titanic_data.csv.
#
# Напишіть програму, що видаляє другу колонку з цієї таблиці та зберігає оновлену таблицю
# у файл titanic_data_2.csv.
#
# Бажано використовувати map для якомога більшої долі операцій.
#
# Hint: ви можете зробити за допомогою map все, окрім власне роботи з файлами

with open("titanic_data.csv", "r") as f:
    rows_list = f.readlines()

rows_edit = map(lambda item: item.replace("\n", "").split(","), rows_list)
rows_delete = map(lambda line: line[:1] + line[2:], rows_edit)

with open("titanic_data_1.csv", "w") as file:
    for element in list(rows_delete):
        line = ",".join(element) + "\n"
        file.write(line)