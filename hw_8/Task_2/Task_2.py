import sys

# Первый интерактивный тест. Изменяем список 'sys.path' добавив католог в PYTHONPATH.
# Создан модуль test_module, который должен напечатать "Hi, I'm test module".

print(sys.path)

try:
    import test_module
except ModuleNotFoundError:
    print("Error, not found module")

module_path = 'C:\\Users\\38098\\Desktop\\dir_test_module'
sys.path.append(module_path)

print(sys.path)

try:
    import test_module
except ModuleNotFoundError:
    print("We failed")

# Модуль найден и выведено "Hi, I'm test module".

# Второй интерактивный тест. Изменяем список 'sys.path' удаляя католог в пути Python.

sys.path.remove(module_path)

print(sys.path)

try:
    import test_module
except ModuleNotFoundError:
    print("Module not found")

# Модуль не найден и выведено "Module not found".