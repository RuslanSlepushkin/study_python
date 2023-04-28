with open("myfile.txt", 'w') as file:
    file.write("Hello file world!\n")

with open("myfile.txt", 'r') as file:
    content = file.read()
    print(content)

# Если добавить другой путь к файлу, он создастся в другом каталоге dir_test_module.

with open("C:\\Users\\38098\\Desktop\\dir_test_module\\myfile.txt", 'w') as file:
    file.write("Hello file world!\n")

with open("C:\\Users\\38098\\Desktop\\dir_test_module\\myfile.txt", 'r') as file:
    content = file.read()
    print(content)
