__author__ = 'Ильиных Павел Сергеевич'

# coding UTF-8

import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Создание папок dir_ c 1 по 9
def create_dir():
    i = 1
    while i <= 9:
        d = 'dir_' + str(i)
        os.mkdir(d)
        i += 1

create_dir()

# Удаление папок из текущей диретории имя которых начинается с dir_
def del_dir():
    file_list = os.listdir()
    i_2 = 0
    while i_2 < len(file_list):
        name = os.path.join(file_list[i_2])
        if name.startswith('dir_'):
            os.rmdir(name)
        i_2 += 1

del_dir()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def file_list():
    print(os.listdir())

file_list()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file():
    new_file = __file__ + '.copy'
    shutil.copy(__file__, new_file)

copy_file()