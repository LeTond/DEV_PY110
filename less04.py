'''
>>> import os.path
>>> os.path.join("/tmp/1", "temp.file")  # конкатенация путей
'/tmp/1/temp.file'
>>> os.path.dirname("/tmp/1/temp.file")  # имя каталога по заданному полному пути
'/tmp/1'
>>> os.path.basename("/tmp/1/temp.file")  # имя файла по заданному полному пути
'temp.file'
>>> os.path.normpath("/tmp//2/../1/temp.file")  # нормализация пути
'/tmp/1/temp.file'
>>> os.path.exists("/tmp/1/temp.file")  # существует ли путь?
False
'''
import os.path
#
# print(os.path.join("/tmp/1", "temp.file"))
# print(os.path.dirname("/tmp/1/temp.file"))
# print(os.path.basename("/tmp/1/temp.file"))
# print(os.path.normpath("/tmp//2/../1/temp.file"))
# print(os.path.exists("/tmp/1/temp.file"))

'''
Python по умолчанию достаточно просто работает с файлами операционной системы,
в C-подобном стиле.
Перед работой с файлом надо его открыть с помощью команды open

Результатом этой операции будет указатель на файл,
в котором указатель текущей позиции поставлен на начало или конец файла.

# f = open("path/to/file", "filemode", encoding="utf8")

f = open(“path/to/file”, “rt”, encoding=“utf8”)
“path/to/file” – путь до файла, можно указывать в Unix-style (path/to/file) или в Windows-style (path\\to\\file)
“rt” – режим, в котором файл нужно открывать. Записывается в виде строки, состоит из следующих букв:
r – открыть на чтение (по умолчанию)
w – перезаписать и открыть на запись
x – создать и открыть на запись (если уже есть – исключение)
a – открыть на дозапись (указатель будет поставлен в конец)
t – открыть в текстовом виде (по умолчанию)
b – открыть в бинарном виде
encoding – указание, в какой кодировке файл записан (utf8, cp1251 и т.д.)

При открытии файла в режимах на запись ставится блокировка на уровне операционной системы
'''
# f = open("test.txt", 'a')
# # f2 = open("1.txt", 'r')
# # f.write("This is a test string\n")
# print(f.tell())
#
# f = open('test.txt', 'r', encoding='utf-8')
# print(f.tell())
#
# print(f.read(10))
# print(f.tell())
#
# f.seek(15)
# print(f.read())


'''
Чтение и запись построчно
'''
# f = open("test.txt", 'a', encoding='utf-8')
# sequence = ["other string\n", "123\n", "test test string\n"]
# f.writelines(sequence)
#
'''
Запись в файл
'''
# for line in sequence:
#     f.write(line)
#     f.write('\n')
#
# f.close()

# f = open("test.txt", 'r', encoding='utf-8')
# print(f.readline())
# print(f.read(5))
# print(f.readline())
#
# for line in f:
#     print(line.strip())
# f.close()
#
# print(f)
# print(iter(f))
# # id(f) == id(iter(f))

'''
Менеджер контекста with
Для явного указания места работы с файлом, а также чтобы не забывать закрыть файл после обработки, существует менеджер контекста with.
В блоке менеджера контекста открытый файл «жив» и с ним можно работать, при выходе из блока – файл закрывается.
Менеджер контекста неявно вызывает закрытие файла после работы
'''
# f = open("test.txt", 'r', encoding='utf-8')
# with open("test.txt", 'rb') as f:
#     a = f.read(10)
#     b = f.read(23)
#     c = f.read(45)
#     print(a)
#     print(b)
#     print(c)
# f.read(3)


'''
Сериализация
Сериализация – процесс перевода какой-либо структуры данных в другой формат,
более удобный для хранения и/или передачи.
Основная задача сериализации – эффективно (т.е. обычно с наименьшим размером)
сохранить или передать данные, при условии, что их можно десериализовать в исходные.
Чаще всего это работа на низком уровне с байтами и различными структурами. Но не обязательно.
'''

'''
JSON – JavaScript Object Notation – текстовый формат обмена данными.
Легко читаем людьми, однозначно записывает данные, подходит для сериализации сложных структур.
Много используется в вебе.
'''

import json

# print(json.dumps([1, 2, 3, {'4': 5, '6': 7}]))
# print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))
# print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], indent=4))    # Задаем отступ
# print(json.dumps([(1, 2, 3), (4, 5, 6)], indent='\t'))    # json не поддерживает tuple


# def check_code_decode_json(src):
#     json_str = json.dumps(src)
#     python_obj = json.loads(json_str)
#     # python_obj = json.loads(json_str, parse_int=True)
#
#     print('src:', src)
#     print('json:', json_str)
#     print('result', python_obj)
#
#     return src == python_obj
#
# src = [1, 2, 3, {'4': 5, '6': 7}]
# # src = [(1, 2, 3)]     # С тюпл не работает
# check_code_decode_json(src)
# print(check_code_decode_json(src))

'''
Не путайте dumps с dump, а loads с load!
Последние функции предназначены для работы с каким-либо источником 
(файлом, потоком данных и т.д.)
'''
# FileName = "test.txt"
# src = [1, 2, 3, {'4': 5, '6': 1700}]
#
# with open(FileName, 'w') as file:
#     # file.write(json.dumps(src))
#     json.dump(src, file)
#
# with open(FileName) as f:
#     python_obj = json.load(f)
#
# print(python_obj)

'''
Pickle
Сериализация в JSON полезна в мире веба, если вам нужно что-то сохранить на диск – используется бинарная сериализация.
Самый популярный модуль для бинарной сериализации – Pickle.
Сохраняет объекты в бинарный формат, который потом можно восстановить при другом запуске или на другом устройстве.
Вследствие развития получилось, что у pickle есть несколько протоколов. Сохранять и загружать нужно с одним и тем же, 
по умолчанию в Python3 протокол – 3.
'''

'''
В языке Python существуют и другие способы сериализации:
Если объект можно перевести в байт-массив – можно с помощью struct перевести и сохранить в файл 
(преимущества – можно распарсить на другом языке)
Если объект – NumPy массив, можно использовать np.save, np.savetxt, np.savez, np.savez_compressed
Для хранения больших файлов (астрономические данные, веса больших нейронных сетей и т.д.) используется формат HDF5. 
Работа с такими файлами в Python осуществляется с помощью библиотеки h5py и методов create_dataset, File и т.д.
Многие модули имеют собственные методы для сериализации данных (часто в основе – pickle или struct)
'''



'''
Парсинг аргументов командной строки
Официально запуск вашего скрипта выглядит следующим образом:
/path/to/python.exe /path/to/file.py
Сначала идет команда, которую нужно выполнить, далее – аргументы, которые в нее подаются, например, путь до скрипта.
Аргументов может быть несколько.
/path/to/python.exe /path/to/file.py –v –b –i “Test”
Каждое слово (разделенное пробелом) – отдельный аргумент.
'''
import sys
print(sys.argv)     # /path/to/python.exe   /path/to/file.py

# if len(sys.argv) < 2:
#     print("Мало")
# elif len(sys.argv) > 3:
#     print("Много")
# else:
#     print(f"Hello {sys.argv[1]}. Count: {sys.argv[2]}")

# import argparse
#
# def create_parser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('name', nargs="?", default=False) # создадим один необязательный позиционный аргумент
#     return parser
#
# if __name__ == "__main__":
#     parser = create_parser()
#     namespace = parser.parse_args()
#     print(namespace)
#
#     if namespace.name:
#         print("привет, {}!".format(namespace.name))
#     else:
#         print("Привет, Мир!")



import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-name', nargs="?", dest='my_arg')  # создадим один необязательный позиционный аргумент
    return parser

if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args()
    print(namespace)

    if namespace.name:
        print("привет, {}!".format(namespace.name))
    else:
        print("Привет, Мир!")

svsdfdsf

dsf
sd
fsd
f











