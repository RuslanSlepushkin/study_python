# Задача 2: для даних ПІБ і серії-номера паспорту зробити наступне:
# 1. ПІБ очистити від небажаних символів і привести в офіційний формат
# 2. Серію паспорта привести в належний формат (тільки великі літери, ніяких інших символів).
# 3. Вивести серію-номер паспорта в зворотньому порядку.
# 4. Вивести суму цифр в номері паспорта.
# 5. Перевірити, чи є рядок "great poet" в рядку статуса громадянина
# Для цілей задачі вважаємо, що серія може бути довільної довжини, номер - 6 символів.
# Також, нагадую, що якщо ви не знаєте, як шукати специфічні для типу методи (як-то "abc".lower()),
# ви можете завжди викликати вбудовану функцію dir() з переданим у неї конструктором типу.

corrupted_name_1 = "    $%taras shevchenko& "
id_number = "greatta654lentgreatresponsibility-240891"
corrupted_status = "jfsnljnlsfgnjfsgnjlsgfnlngfslnsdglnlsdgnljgsdnlnln great poet 'akk;ldnflkjsabg;kbouht024h0pijngadknsn"

# 1. ПІБ очистити від небажаних символів і привести в офіційний формат
full_name = ""
for i in corrupted_name_1:
    if i.isalpha() or i == ' ':
        full_name += i
print(full_name.title().strip())
# 2. Серію паспорта привести в належний формат (тільки великі літери, ніяких інших символів).
new_id_number = ""
for i in id_number[:-6]:
    if i.isalpha() or i.isdigit():
        new_id_number += i
print(new_id_number.upper())
# 3. Вивести серію-номер паспорта в зворотньому порядку.
rev_id_number = id_number[::-1]
print(rev_id_number)
# 4. Вивести суму цифр в номері паспорта.
list_id_number = list(id_number[-6:])
sum_id_number = 0
for number in list_id_number:
    sum_id_number += int(number)
print(sum_id_number)
# 5. Перевірити, чи є рядок "great poet" в рядку статуса громадянина
check_one_corrupted_status = 'great poet' in corrupted_status
print(check_one_corrupted_status)